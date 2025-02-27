import numpy as np
import cv2 as cv

# Setup camera
cap = cv.VideoCapture(0)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
bound = 0.10
width_lower_bound = width - (bound * width)
width_upper_bound = width + (bound * width)
height_lower_bound = height - (bound * height)
height_upper_bound = height + (bound * height)
print("Camera dimensions:", (width, height)) 
print(f"width lower = {width_lower_bound}, width upper = {width_upper_bound} ")
print(f"height lower = {height_lower_bound}, height upper = {height_upper_bound}")
# Define orange color bounds
orangeLower = (5, 150, 150)
orangeUpper = (15, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Convert frame to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv[..., 2] = cv.createCLAHE(clipLimit=5).apply(hsv[..., 2]) 
    # Create mask for orange color
    mask = cv.inRange(hsv, np.array(orangeLower), np.array(orangeUpper))
    
    # Find contours of the masked image
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Track the largest contour (assuming it's the main orange blob)
    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        M = cv.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            cv.putText(frame, f"({cx}, {cy})", (cx + 10, cy - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if(cx < width_lower_bound):
                print("move right")
            elif(cx > width_lower_bound):
                print("move left")
            elif (cy > height_lower_bound):
                print("move up")
            elif (cy < height_upper_bound):
                print("move down")
                '''
                0 -> 480 (down to up) (height)
                0 -> 640 (left to right) (width)
                '''
    # Apply mask to the original frame
    result = cv.bitwise_and(frame, frame, mask=mask)
    
    # Display the masked output with tracking
    cv.imshow('Orange Mask', frame)
    
    # Exit on pressing 'ESC'
    if cv.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()