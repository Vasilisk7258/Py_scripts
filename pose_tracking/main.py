import cv2
import mediapipe as mp
import time
from POSE_TRACKING_MODULE import PoseDetector

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = PoseDetector()

while True:

    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPos(img)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('asdaklslksksalkld', cv2.flip(img, 1))
    cv2.waitKey(1)