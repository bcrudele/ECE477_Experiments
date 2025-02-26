import numpy as np
import cv2 as cv

# Setup camera
cap = cv.VideoCapture(0)

# Define orange color bounds
orangeLower = (5, 150, 150)
orangeUpper = (15, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # # Convert frame to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # # Create mask for orange color
    mask = cv.inRange(hsv, np.array(orangeLower), np.array(orangeUpper))
    
    # # Apply mask to the original frame
    result = cv.bitwise_and(frame, frame, mask=mask)
    
    # # Display the masked output
    # cv.imshow('Orange Mask', result)
    cv.imshow('frame', result)
    
    # Exit on pressing 'ESC'
    if cv.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
