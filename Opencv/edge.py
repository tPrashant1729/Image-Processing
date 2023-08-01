import numpy as np
import cv2 as cv

img = cv.imread("D:/Dnk_project/output/nature.jpg")


def scaled_img(img, scale):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimension = (width, height)
    resized_img = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
    return resized_img


resized_img = scaled_img(img, 0.15)
cv.imshow("original", resized_img)
# cv.imwrite("nature_resized.jpg", resized_img)

# # GRAY
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("lap", lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 1, 0)
combined_sobel = cv.bitwise_or(sobelx, sobely)
canny = cv.Canny(gray, 140, 160)
cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("sobel_combined", combined_sobel)
cv.imshow("canny", canny)
cv.waitKey(0)
