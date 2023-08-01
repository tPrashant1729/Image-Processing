import cv2

cap = cv2.VideoCapture('D:/Dnk_project/output/family_running.mp4')
print(cv2.__version__)
while True:
    success, img = cap.read()
    if not success:
        break

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
