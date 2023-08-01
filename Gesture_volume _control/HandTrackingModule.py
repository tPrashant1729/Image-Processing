import cv2 as cv
import mediapipe as mp
import time


class Detect():
     def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
         self.mode = mode
         self.maxHands = maxHands
         self.modelComplex = modelComplexity
         self.detectionCon = detectionCon
         self.trackCon = trackCon
         self.mpDraw = mp.solutions.drawing_utils
         self.mpHands = mp.solutions.hands
         self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,
                                         self.detectionCon, self.trackCon)
     def hand_detect(self, img):
         self.result = self.hands.process(img)

         if self.result.multi_hand_landmarks:
            for handlm in self.result.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handlm, self.mpHands.HAND_CONNECTIONS)
         return img

     def findpos(self, img, draw=True):
         lmlist = []
         h, w, c = img.shape
         if self.result.multi_hand_landmarks:
             for handlm in self.result.multi_hand_landmarks:
                 self.mpDraw.draw_landmarks(img, handlm, self.mpHands.HAND_CONNECTIONS)
                 for id, lm in enumerate(handlm.landmark):
                     cx, cy = int(lm.x * w), int(lm.y * h)
                     lmlist.append([id, cx, cy])
                     if draw:
                         cv.circle(img, (cx, cy), 10, (0, 255, 0), cv.FILLED)
         return lmlist


def main():
    cap = cv.VideoCapture(0)
    ptime = 0

    detector = Detect()

    while True:
        success, img = cap.read()
        newimg = detector.hand_detect(img)
        lmlist = detector.findpos(newimg, 7)
        if len(lmlist) != 0:
            print(lmlist)
        # print(type(newimg))
        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime

        cv.putText(newimg, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv.imshow("typing", newimg)
        # Exit the video display if 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
