import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# blank[:] = (0,0,255)
# cv.imshow('green',blank)

cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness=-1)
cv.rectangle(blank, (blank.shape[0]//2, blank.shape[1]//2), (500,0), (0, 0, 255), thickness=-1)
cv.rectangle(blank, (0, blank.shape[0]//2), (blank.shape[0], blank.shape[1]), (255, 0, 0), thickness=-1)

cv.circle(blank, (255, 255), 50, color=(0, 0, 0), thickness=-1)

cv.line(blank, (500, 0), (0, 500), color=(0, 255, 255), thickness=2)

cv.putText(blank, 'Painting', (0, 123), fontScale=2.0, fontFace=0, color=(0, 0, 0), thickness=2)
cv.imshow('Rectangle with circle and line', blank)
cv.waitKey(0)
