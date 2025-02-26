import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Set lower resolution for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)  # Try increasing FPS

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        continue  # Skip processing if frame is invalid

    # Convert frame to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define orange color range
    orangeLower = (5, 150, 150)
    orangeUpper = (15, 255, 255)

    # Create mask and apply bitwise AND
    mask = cv2.inRange(hsv_image, orangeLower, orangeUpper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show result
    cv2.imshow("Orange Isolated", result)

    # Save only when 's' is pressed to avoid lag
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("orange_isolated.jpg", result)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
