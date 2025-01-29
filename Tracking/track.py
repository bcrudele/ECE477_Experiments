import numpy as np
import cv2 as cv
import time
import matplotlib.pyplot as plt
# setup camera
cap = cv.VideoCapture(0)
#first fram cap roi select
ret, frame = cap.read()
bbox = cv.selectROI('select', frame, False)
# select bounding box bounds
x, y, w, h = bbox
# convert roi to hsv, mask
roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
# histogram based on hsv range
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
# meanshift algorithm- stops after 10 its or when location change is < 1 px
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
# get fram w and h
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# TESTING IDK WHAT IM DOING
# get outer bound of frame. if masked object thingy is outside of the frame, print MOVE in x dir
outer_3_percent_x_min = frame_width * 0.03
outer_3_percent_x_max = frame_width * 0.97
outer_3_percent_y_min = frame_height * 0.03
outer_3_percent_y_max = frame_height * 0.97

# main loop
while(1):
    ret, frame = cap.read()

    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv.meanShift(dst, bbox, term_crit)

        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)

        # Check if any part of the bounding box is within the outer 3% region
        # if x < outer_3_percent_x_min or x + w > outer_3_percent_x_max or y < outer_3_percent_y_min or y + h > outer_3_percent_y_max:
        #     print(time.time(),"move")

        if x < outer_3_percent_x_min:
            print(time.time(), "move right")
        elif x + w > outer_3_percent_x_max:
            print(time.time(), "move left")
        elif y < outer_3_percent_y_min:
            print(time.time(), "move down")
        elif y + h > outer_3_percent_y_max:
            print(time.time(), "move up")

        cv.imshow('gfg', img2)
        # i want to see histogram

        plt.clf()  # Clear the previous plot
        plt.plot(roi_hist)  # Plot the normalized histogram
        plt.xlabel('HSV Hue values')
        plt.ylabel('Frequency')
        plt.title('HSV Histogram of ROI at time ' + str(time.time()))
        plt.draw()  # Redraw the plot
        plt.pause(0.01)  

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
# plt.plot(roi_hist)
cap.release()
cv.destroyAllWindows()
