import cv2

img = cv2.imread("littleGirl.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('face_detect.xml')
# The third parameter is the number of time the face is detected,
# only considered a face
faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)
print(len(faceRect))

for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
