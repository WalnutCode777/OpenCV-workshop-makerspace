import cv2

img = cv2.imread("suiseiColorful.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# img1 = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)


cv2.imshow("img", img)
# cv2.imshow("img1", img1)
cv2.imshow("img", img)
print(type(img))
print(img.shape)
cv2.waitKey(0) == ord('q')

# B G R
# [
#     [[0, 255, 0], [0, 255, 255], ...724],
#     [[0, 255, 0], [0, 255, 255], ...724],
#     [[0, 255, 0], [0, 255, 255], ...724],
#     [[0, 255, 0], [0, 255, 255], ...724],
#     [[0, 255, 0], [0, 255, 255], ...724],
#     ...1024

# ]
