import numpy as np
import cv2 as cv

img = cv.imread('D:/Dnk_project/dataset_passport_size/Train/obj/9000.png')

# def scaled_img(img, scale):
#     height = int(img.shape[0]*scale)
#     width = int(img.shape[1]*scale)
#     dimension = (width, height)
#     img = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
#     return img

# img = scaled_img(img, 0.09)
# cv.imshow('original', img)

# GRAY 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)

haar_cascade = cv.CascadeClassifier('D:/Dnk_project/image_processing/haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    print(x, y, w, h, x+w, y+h)
cv.imshow('Detected Faces', img)
cv.waitKey(0)
