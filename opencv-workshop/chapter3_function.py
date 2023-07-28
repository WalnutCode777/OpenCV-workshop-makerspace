import cv2
import numpy as np

img = cv2.imread("mumeiCard.jpg")
img = cv2.resize(img, (0, 0), fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (9, 9), 5, 1)
blur2 = cv2.GaussianBlur(img, (99, 99), 300, 10)

canny = cv2.Canny(img, 450, 600)
canny2 = cv2.Canny(img, 100, 150)

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
