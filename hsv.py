import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
ret, frame = cap.read()

# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv.CAP_PROP_FPS, 30)  # Try increasing FPS

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break  # Skip processing if frame is invalid

    # Convert frame to HSV
    hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define orange color range
    orangeLower = (5, 150, 150)
    orangeUpper = (15, 255, 255)

    # Create mask and apply bitwise AND
    mask = cv.inRange(hsv_image, orangeLower, orangeUpper)
    result = cv.bitwise_and(frame, frame, mask=mask)

    # Show result
    cv.imshow("Orange Isolated", result)

    # Save only when 's' is pressed to avoid lag
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite("orange_isolated.jpg", result)
    

cap.release()
cv.destroyAllWindows()
