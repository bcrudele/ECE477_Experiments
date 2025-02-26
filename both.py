import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Convert the image to HSV (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Apply CLAHE to the Value channel (the brightness part of HSV)
hsv_image[..., 2] = cv2.createCLAHE(clipLimit=5).apply(hsv_image[..., 2])

# Define the range for the orange color in HSV
orangeLower = (5, 150, 150)  # Lower bound for orange (light orange)
orangeUpper = (15, 255, 255)  # Upper bound for orange (dark orange)

# Create a mask that isolates the orange color from the enhanced HSV image
mask = cv2.inRange(hsv_image, orangeLower, orangeUpper)

# Bitwise-AND the mask with the original image to isolate the orange regions
result = cv2.bitwise_and(image, image, mask=mask)

# Show the images
cv2.imshow("Original Image", image)  # Original image
cv2.imshow("Mask", mask)  # Mask showing only the orange regions
cv2.imshow("Orange Isolated", result)  # Final isolated orange regions

# Save the results
cv2.imwrite("orange_isolated3.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
