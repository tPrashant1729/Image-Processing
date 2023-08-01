import numpy as np
import cv2 as cv

img = cv.imread('D:\Dnk_project\output\chelsea.png')
cv.imshow('original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
cv.imshow('blue_', blue)
green = cv.merge([blank, g, blank])
cv.imshow('green_', green)
red = cv.merge([blank, blank, r])
cv.imshow('red_', red)

cv.waitKey(0)