import numpy as np
import cv2 as cv

img = cv.imread('D:/Dnk_project/output/astronaut.png')
#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv.resize(img, dsize)
cv.imshow('original', output)

blur = cv.blur(output, (5, 5))
cv.imshow('blur', blur)

g_blur = cv.GaussianBlur(output, (5, 5), 0)
cv.imshow('g_blur', g_blur)

m_blur = cv.medianBlur(output, 5, 0)
cv.imshow('m_blur', m_blur)

b_blur = cv.bilateralFilter(output, 10, 40, 35)
cv.imshow('b_blur', b_blur)
cv.waitKey(0)