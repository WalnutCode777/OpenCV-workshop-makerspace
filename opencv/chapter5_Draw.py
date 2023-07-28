import cv2
import numpy as np

# Create black canvas
img = np.zeros((720, 720, 3), np.uint8)
line1 = cv2.line(img, (0, 0), (400, 300), (0, 250, 162), 3)
line2 = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 250, 162), 3)
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (500, 600), 30, (255, 0, 255), cv2.FILLED)
cv2.putText(img, "How are you", (100, 200),cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
