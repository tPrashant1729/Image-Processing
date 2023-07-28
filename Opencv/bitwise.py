import numpy as np
import cv2 as cv

blank = np.zeros((300, 300), dtype = 'uint8')
rect = cv.rectangle(blank.copy(), (30, 30), (270, 270), 255, thickness= -1)
circle = cv.circle(blank.copy(), (150, 150), 150, 255, thickness= -1)

cv.imshow('rect', rect)
cv.imshow('circle', circle)

bit_or = cv.bitwise_or(rect, circle)
cv.imshow('bit_or', bit_or)

bit_and = cv.bitwise_and(rect, circle)
cv.imshow('bit_and', bit_and)

bit_xor = cv.bitwise_xor(rect, circle)
cv.imshow('bit_xor', bit_xor)

bit_not = cv.bitwise_not(circle)
cv.imshow('bit_not', bit_not)

cv.waitKey(0)
