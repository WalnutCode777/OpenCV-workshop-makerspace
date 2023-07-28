import cv2
import numpy as np

vc = cv2.VideoCapture(0)

# Pink Green Yellow
penColorHSV = [[122, 119, 36, 179, 255, 255],
               [46, 78, 172, 71, 255, 255],
               [22, 70, 214, 31, 255, 255]]

penColorNibBGR = [[255, 0, 0],
                  [0, 255, 0],
                  [0, 255, 255]]

# X, Y, ColorID
drawingPoints = []


def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        penX, penY = findPenContour(mask)
        cv2.circle(imgContour, (penX, penY), 10, penColorNibBGR[i], cv2.FILLED)
        if penY != -1:
            drawingPoints.append([penX, penY, i])
    # cv2.imshow("result", result)


def findPenContour(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1

    for contour in contours:

        cv2.drawContours(imgContour, contour, -1, (0, 255, 0), 4)

        area = cv2.contourArea(contour)
        if area > 100:
            peri = cv2.arcLength(contour, True)
            vertices = cv2.approxPolyDP(contour, peri * 0.3, True)
            x, y, w, h = cv2.boundingRect(vertices)

    return x+w//2, y


def draw(drawingPoints):
    for point in drawingPoints:
        cv2.circle(imgContour, (point[0], point[1]),
                   10, penColorNibBGR[point[2]], cv2.FILLED)


while True:
    ret, frame = vc.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video', frame)
        findPen(frame)
        draw(drawingPoints)
        cv2.imshow('contour', imgContour)
    else:
        break
    if cv2.waitKey(1) == ord("q"):
        break
