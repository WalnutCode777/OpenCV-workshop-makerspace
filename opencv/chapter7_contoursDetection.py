import cv2

# Different from edge detection, used to find the border of the shape

img = cv2.imread("shape.jpg")
imgContour = img.copy()
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
imgContour = cv2.resize(imgContour, (0, 0), fx=0.5, fy=0.5)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)
# This function will return two value
contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # print(i)
    cv2.drawContours(imgContour, contour, -1, (0, 255, 0), 4)
    # Print area of contour
    # print(cv2.contourArea(contour))
    # Length of contour
    # closed or opened arc length
    # print(cv2.arcLength(contour, True))
    area = cv2.contourArea(contour)
    if area > 100:
        peri = cv2.arcLength(contour, True)
        # The greater the approx value, the more poly lines
        vertices = cv2.approxPolyDP(contour, peri * 0.3, True)
        # Coordinates of vertices
        print(vertices)
        # Number of vertices
        print(len(vertices))
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (255, 0, 0), 4)
        if corners == 3:
            cv2.putText(imgContour, "triangle", (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgContour, "rectangle", (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgContour, "pentagon", (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, "circle", (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.imshow("canny", canny)
cv2.imshow("imgContour", imgContour)
cv2.waitKey(0)
