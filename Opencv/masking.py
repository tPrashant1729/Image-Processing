import numpy as np
import cv2 as cv

img = cv.imread('D:/Dnk_project/output/astronaut.png')
cv.imshow('original', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
# cv.imshow('blank', blank)

# mask = cv.circle(blank, (230, 110), 100, 255, -1)
mask = cv.rectangle(blank, (180, 60), (280, 160), 255, -1)

# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

print(img.shape[:2])
cv.waitKey(0)
