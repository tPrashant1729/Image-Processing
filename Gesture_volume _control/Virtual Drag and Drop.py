import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
color = (255, 0, 255)
# cx, cy, w, h = 100, 100, 200, 200  # Keep w and h fixed for the desired shape


class Dragrect:
    def __init__(self, centerpos, size=[200, 200]):
        self.centerpos = centerpos
        self.size = size

    def update(self, cursor):
        cx, cy = self.centerpos
        w, h = self.size

        if (
            cx - w // 2 < cursor[0] < cx + w // 2
            and cy - h // 2 < cursor[1] < cy + h // 2
        ):  # Fixed the typo cx+h//2 -> cy+h//2
            self.centerpos = cursor


rectlist = []
for i in range(4):
    rectlist.append(Dragrect([i * 250 + 150, 150]))

while True:
    success, frame = cap.read()
    frame = cv.flip(frame, 1)
    lmlist, img = detector.findHands(frame)

    if lmlist:
        p1 = lmlist[0]["lmList"][8][:2]
        p2 = lmlist[0]["lmList"][12][:2]
        cursor = p1
        l, _, _ = detector.findDistance(p1, p2, img)

        if l < 25:
            # call update here
            for rect in rectlist:
                rect.update(cursor)
    for rect in rectlist:
        cx, cy = rect.centerpos
        w, h = rect.size

        # Draw the rectangle with the fixed shape (w, h)
        cv.rectangle(
            img,
            (cx - w // 2, cy - h // 2),
            (cx + w // 2, cy + h // 2),
            color,
            cv.FILLED,
        )

    cv.imshow("webcam", img)
    if cv.waitKey(1) & 0xFF == ord(" "):
        break
