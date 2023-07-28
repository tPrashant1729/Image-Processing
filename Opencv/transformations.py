import numpy as np
import cv2 as cv

# x --> Right
# -x --> Left
# y --> Down
# -y --> Up
def translate(img, x, y):
    dsize = (img.shape[1], img.shape[0])
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(img, transmat, dsize)


img1 = cv.imread('D:/Dnk_project/output/astronaut.png')
translated = translate(img1, 100, 100)
cv.imshow('translated', translated)


def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]

    if rotpoint==None:
        rotpoint = (height//2,width//2)
    
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    return cv.warpAffine(img, rotmat, (height, width))

rotate_img = rotate(img1, 45)
cv.imshow('rotate_img',rotate_img)
cv.waitKey(0)
