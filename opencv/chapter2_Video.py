import cv2

vc = cv2.VideoCapture(0)

while True:
    ret, frame = vc.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=1.5, fy=1.5)
        cv2.imshow('video', frame)
    else:
        break
    cv2.waitKey(1)
