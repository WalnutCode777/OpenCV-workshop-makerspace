import numpy as np
import cv2
import random

# img = np.empty((300, 300, 3), np.uint8)
img = cv2.imread('suiseiColorful.jpg')
img1 = cv2.imread('suiseiColorful.jpg')
img1 = cv2.resize(img1, (0, 0), fx=0.2, fy=0.2)
img2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
newImg = img[324:950, 424:1000]
newImg = cv2.resize(newImg, (0, 0), fx=0.5, fy=0.5)

# for row in range(300):
#     for col in range(img1.shape[1]):
#         # img[row][col] = [0, 255, 0]
#         img1[row][col] = [random.randint(0, 255), random.randint(
#             0, 255), random.randint(0, 255)]
# print(img.shape)
cv2.imshow('img', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', newImg)
cv2.waitKey(0)
