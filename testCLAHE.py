# from collections import deque
# from imutils.video import VideoStream
# import numpy as np
# import cv2
# import argparse
# import time
# import imutils


# ap = argparse.ArgumentParser()
# ap.add_argument("-v", "--video", help="Path to the (optional) video file")
# ap.add_argument("-b", "--buffer", default=64, type=int, help="max buffer size")
# args = vars(ap.parse_args())

# orangeLower = (16, 100, 100)
# orangeUpper = (6, 100, 96)
# pts = deque(maxlen=args["buffer"])

# if not args.get("video", False):
#     vs = VideoStream(src=0).start()
# else:
#     vs = cv2.VideoCapture(args["video"])

# time.sleep(2.0)


# while True:
#     frame = vs.read()
#     frame = frame[1] if args.get("video", False) else frame
#     if frame is None:
#         break

    # frame = imutils.resize(frame, width=600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    # hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # print(hsv)
    # mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    # mask = cv2.erode(mask, None, iterations=2)
    # mask = cv2.dilate(mask, None, iterations=2)
    # if(mask is not None):
    #     print("mask found")
    # cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # center = None

    # if len(cnts) > 0:
    #     print("found")
    #     c = max(cnts, key=cv2.contourArea)
    #     ((x, y), radius) = cv2.minEnclosingCircle(c)
    #     M = cv2.moments(c)
    #     center = (int(M['m10']/M['m00']), int(M['m01']/M['m00']))

    #     if radius > 10:
    #         cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
    #         cv2.circle(frame, center, 5, (0, 0, 255), -1)

#     pts.append(center)

#     for i in range(1, len(pts)):
#         if pts[i-1] is None or pts[i] is None:
#             continue

#         thickness = int(np.sqrt(args["buffer"] / float(i+1)) * 2.5)
#         cv2.line(frame, pts[i-1], pts[i], (0, 0, 255), thickness)

#     cv2.imshow("Frame", frame)
#     key = cv2.waitKey(1) & 0xFF

#     if key == ord('q'):
#         break

# if not args.get("video", False):
#     vs.stop()
# else:
#     vs.release()


# cv2.destroyAllWindows()

# import cv2
# import numpy as np
 
# # Reading the image from the present directory
# image = cv2.imread("image.jpg")

# # Resizing the image for compatibility
# image = cv2.resize(image, (500, 600))
 
# # The initial processing of the image
# # image = cv2.medianBlur(image, 3)
# image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# # The declaration of CLAHE
# # clipLimit -> Threshold for contrast limiting
# clahe = cv2.createCLAHE(clipLimit=5)
# final_img = clahe.apply(image_bw) + 30
 
# # Ordinary thresholding the same image
# _, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)
 
# # Showing the two images
# cv2.imshow("ordinary threshold", ordinary_img)
# cv2.imshow("CLAHE image", final_img)

import cv2
import numpy as np

# Reading the image from the present directory
image = cv2.imread("image.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not read image. Check the file path.")
    exit()

# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))

# Convert to grayscale
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=5)
final_img = clahe.apply(image_bw) + 30

# Ordinary thresholding
_, ordinary_img = cv2.threshold(image_bw, 180, 255, cv2.THRESH_BINARY)

# Save the processed images to files
cv2.imwrite("CLAHE_output180.jpg", final_img)
cv2.imwrite("threshold_output180.jpg", ordinary_img)

# Display the images
cv2.imshow("Ordinary Threshold", ordinary_img)
cv2.imshow("CLAHE Image", final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
