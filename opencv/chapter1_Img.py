import cv2

img = cv2.imread('littleGirl.jpeg')

img = cv2.resize(img, (300, 300))
img1 = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.waitKey(10000)

img2 = cv2.imread("suiseiColorful.jpg")
print(type(img1))
print(img1.shape)
print(img1)

# B G R

# [
#     [[0, 255, 0], [0, 255, 255], [255, 0, 0], ...1448],
#     [[0, 255, 0], [0, 255, 255], [255, 0, 0], ...1448],
#     [[0, 255, 0], [0, 255, 255], [255, 0, 0], ...1448],
#     [[0, 255, 0], [0, 255, 255], [255, 0, 0], ...1448],
#     [[0, 255, 0], [0, 255, 255], [255, 0, 0], ...1448],
#     ...2048
    
# ]
