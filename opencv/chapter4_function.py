import cv2
import numpy as np

# Function that is often used

img = cv2.imread("mumeiCard.jpg")
img = cv2.resize(img, (0, 0), fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# The Gaussian kernel size must be positive odd number
# standard deviation in x direction, meaning, the amount of blur apply in x direction
blur = cv2.GaussianBlur(img, (9, 9), 5, 1)
blur2 = cv2.GaussianBlur(img, (99, 99), 300, 10)

# Perform edge detection while suppressing 
# noise (unwanted distortions in the pixel values that are not part of the original image) 
# can consider as unwanted signals that corrupt the true signal of the image 
# caused by sensors limitations, transmission errors, or environmental factors
# Hysteresis thresholding, first value is min threshold, and latter is max threshold,
# pixels value with adjacent pixel value difference that exceeds max threshold is considered strong edges, 
# between or lower pixel value is weak thresholds
# The lower the threshold, the more edges it highlight, because the threshold is lower
canny = cv2.Canny(img, 450, 600)
canny2 = cv2.Canny(img, 100, 150)

# dilate, thicken the edge
# This function creates a 3 x 3 2D matrix fills with 1, with 8 bit unsigned integer
# The greater the matrix dimension, the thicker the edges get
kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(canny2, kernel, iterations=1)

# Erode the edge
kernel1 = np.ones((5, 5), np.uint8)
erode = cv2.erode(dilate, kernel1, iterations=2)


# cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("blur", blur)
# cv2.imshow("blur2", blur2)
cv2.imshow("canny", canny)
# cv2.imshow("canny2", canny2)
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)
cv2.waitKey(0)
