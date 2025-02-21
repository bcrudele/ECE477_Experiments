# Import required packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# Define command-line arguments (only for buffer size since no video file is used)
ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

# Define HSV color boundaries for tracking the ball (green by default)
hsvLow = (8.1, 94, 84)
hsvHigh = (10, 100, 90)

# Initialize deque to store tracked points
pts = deque(maxlen=args["buffer"])

# Start the video stream from the webcam
print("[INFO] Starting live video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)  # Allow the camera to warm up

# Start looping to process frames
while True:
    # Read the frame from the webcam
    frame = vs.read()
    #if(frame is not None): print("read frame")

    # If frame is None, break (happens if the camera disconnects)
    if frame is None:
        break

    # Resize frame for consistency
    frame = imutils.resize(frame, width=600)

    # Apply Gaussian Blur to reduce noise
    #blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to detect the ball based on color range
    mask = cv2.inRange(hsv, hsvLow, hsvHigh)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    if(mask is not None): print("mask found")
    # Find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # Process contours if found
    if len(cnts) > 0:
        # Find the largest contour
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        # Avoid division by zero when computing the centroid
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Draw the circle and center point if the ball is big enough
        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            if center:
                #cv2.circle(frame, center, 5, (0, 0, 255), -1)
    # Update the list of tracked points
                pts.appendleft(center)

    # Draw the tracking line
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            # continue
            thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    # Show the frame
    cv2.imshow("Ball Tracking", frame)
    key = cv2.waitKey(1) & 0xFF

    # Exit on pressing 'q'
    if key == ord("q"):
        break

# Cleanup and release the camera
vs.stop()
cv2.destroyAllWindows()
