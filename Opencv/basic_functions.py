import cv2 as cv

img = cv.imread('D:/Dnk_project/output/astronaut.png')
dimension = (229, 250)
img = cv.resize(img, dimension)
cv.imshow('astronout', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY,)
cv.imshow('astronout_gray', gray)

blur = cv.blur(img, (5, 5), borderType=cv.BORDER_DEFAULT)
cv.imshow('astronout_blur', blur)

# for detecting edge
canny = cv.Canny(blur, 100, 100)
cv.imshow('astronout_canny', canny)

dilate = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilate)

erod = cv.erode(img, (7, 7), iterations=3)
cv.imshow('eroded', erod)

resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize', resize)

cropped = img[70:170, 5:90]
cv.imshow('cropped', cropped)
shape = img.shape[:]
print(shape)
cv.waitKey(000)
