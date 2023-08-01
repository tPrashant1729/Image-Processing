import cv2 as cv
import math
import mediapipe as mp
import time

import numpy as np

import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
################################
wcam, hcam = (640, 480)
################################

cap = cv.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
ptime = 0
ctime = 0
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange())
vol = 0
volper = 0
volbar = 350
minvol = volume.GetVolumeRange()[0]
maxvol = volume.GetVolumeRange()[1]


detector = htm.Detect(detectionCon=0.7)

while True:
    success, img = cap.read()
    newimg = detector.hand_detect(img)
    lmlist = detector.findpos(newimg, draw=False)

    if len(lmlist)!=0:
        # print(lmlist[4], lmlist[8])
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cv.circle(newimg, (x1, y1), 10, (0, 0, 255), cv.FILLED)
        cv.circle(newimg, (x2, y2), 10, (0, 0, 255), cv.FILLED)
        cv.circle(newimg, ((x1+x2)//2, (y1+y2)//2), 10, (0, 0, 255), cv.FILLED)
        cv.line(newimg, (x1, y1), (x2, y2), (255, 0, 0), 2)

        length = math.hypot((x2-x1), (y2-y1))
        # print(length)
        if length<50:
            cv.circle(newimg, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (0, 255, 0), cv.FILLED)

        vol = np.interp(length, [50, 200], [minvol, maxvol])
        volbar = np.interp(length, [50, 200], [350, 150])
        volper = np.interp(length, [50, 200], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol,None)

    cv.rectangle(img, (30, 150), (70, 350), (0, 0, 255), 3)
    cv.rectangle(img, (30, int(volbar)), (70, 350), (0, 0, 255), cv.FILLED)
    cv.putText(img, str(f'{int(volper)} %'), (30, 390), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

    #FPS
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv.putText(newimg, str(f'{int(fps)}'), (30, 70), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
    cv.imshow("typing", newimg)
    # Exit the video display if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord("q"):
        break