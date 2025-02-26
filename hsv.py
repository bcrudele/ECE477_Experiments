import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Convert the image to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for the orange color in HSV
# These values are approximate, adjust if necessary
orangeLower = (5, 150, 150)  # Lower bound for orange (light orange)
orangeUpper = (15, 255, 255)  # Upper bound for orange (dark orange)

# Create a mask that isolates the orange color
mask = cv2.inRange(hsv_image, orangeLower, orangeUpper)

# Bitwise-AND the mask with the original image to isolate the orange regions
result = cv2.bitwise_and(image, image, mask=mask)

# Show the original image, mask, and the result
cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Orange Isolated", result)

# Save the result
cv2.imwrite("orange_isolated.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
