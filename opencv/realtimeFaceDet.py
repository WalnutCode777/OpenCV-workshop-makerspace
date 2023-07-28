import cv2
import dlib

# draw a bounding box over face
def get_max_area_rect(rects):
    # checks to see if a face was not dectected (0)
    if len(rects) == 0:
        return
    areas = []
    for rect in rects:
        areas.append(rect.area())
    return rects[areas.index(max(areas))]


def facial_processing():
    distracton_initialized = False
    eye_initialized = False
    mouth_initialized = False
    normal_initialized = False

    detector = cv2.CascadeClassifier('face_detect.xml')
    # predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    # start video stream
    vc = cv2.VideoCapture(0)

    # loop over frames from the video stream
    while True:
        rect, frame = vc.read()
        if rect:
            # flip around y-axis
            frame = cv2.flip(frame, 1)
            # convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # detect faces in the grayscale frame
            rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            # draw bounding box on face
            rect = get_max_area_rect(rects)
            cv2.imshow('video', frame)

        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == '__main__':
    facial_processing()
