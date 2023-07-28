import time
import cv2
import mediapipe as mp

vc = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
handLms_Style = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=3)
handConection_Style = mpDraw.DrawingSpec(color=(0, 255, 255), thickness=2)
# To calculate frame rate
prevTime = 0
currTime = 0

while True:
    ret, frame = vc.read()
    if ret:
        # Covert color format from BGR to RGB for mediapipe
        rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgbImg)
        # print(result.multi_hand_landmarks)
        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(
                    frame, handLms, mpHands.HAND_CONNECTIONS, handLms_Style, handConection_Style)
                for i, lm in enumerate(handLms.landmark):
                    # The lm.x and lm.y is the ratio of your position to the camera window
                    xPos = int(lm.x * frameWidth)
                    yPos = int(lm.y * frameHeight)
                    # cv2.putText(frame, str(i), (xPos-25, yPos+5),
                    #             cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)
                    # print(i, lm.x, lm.y)
                    # if want to highlight certain finger point
                    if i == 4:
                        cv2.circle(frame, (xPos, yPos), 10,
                                   (0, 0, 255), cv2.FILLED)
                    print(i, xPos, yPos)

        currTime = time.time()
        fps = 1/(currTime-prevTime)
        prevTime = currTime
        cv2.putText(frame, f"FPS: {int(fps)}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('video', frame)

    if cv2.waitKey(1) == ord("q"):
        break
