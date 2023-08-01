import cv2 as cv


def rescale(frame_, scale=.75):
    # works with image , video and live video
    height = int(frame_.shape[0]*scale)
    width = int(frame_.shape[1]*scale)
    dimension = (width, height)
    frame_resized = cv.resize(frame_, dimension, interpolation=cv.INTER_AREA)
    return frame_resized


def resizeres(width, height):
    # works only with live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('D:/Dnk_project/output/family_running.mp4')
while True:
    success, frame = capture.read()
    if not success:
        break
    frame_resized_ = rescale(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video_resize', frame_resized_)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
