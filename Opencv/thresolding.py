import numpy as np
import cv2 as cv

img = cv.imread('D:/Dnk_project/output/nature.jpg')

def scaled_img(img, scale):
    height = int(img.shape[0]*scale)
    width = int(img.shape[1]*scale)
    dimension = (width, height)
    resized_img = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
    return resized_img

resized_img = scaled_img(img, 0.07)
cv.imshow('original', resized_img)

# GRAY 
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#thrsholding
thresh_value, thresh_img = cv.threshold(gray, 95, 255, cv.THRESH_BINARY)
cv.imshow('thresh_img', thresh_img)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_thresh_img', adaptive_thresh)
cv.imwrite('nature_binary.jpg', thresh_img)

cv.waitKey(0)