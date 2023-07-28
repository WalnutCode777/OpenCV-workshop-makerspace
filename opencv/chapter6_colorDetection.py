import cv2
import numpy as np


def empty(v):
    pass


img = cv2.imread("winnieMeme.jpg")

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 320)

cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)

# hue = color shade
# saturation = color intensity
# value = brightness
# Why use hue? Easier to filter color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    # Filter color
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # White color in mask means the color we want to keep
    mask = cv2.inRange(hsv, lower, upper)
    # AND Truth table to mask the color
    # 0 0
    # 0 1
    # 1 0
    # 1 1
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.waitKey(1)
