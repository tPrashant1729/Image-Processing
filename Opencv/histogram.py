import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("D:/Dnk_project/output/nature.jpg")


def scaled_img(img, scale):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimension = (width, height)
    resized_img = cv.resize(img, dimension, interpolation=cv.INTER_AREA)
    return resized_img


resized_img = scaled_img(img, 0.07)
cv.imshow("original", resized_img)

# GRAY HISTOGRAM
# gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# plt.plot(gray_hist)
# plt.title('Gray_histogram')

# COLOR IMAGE HISTOGRAM
# plt.title("Color_histogram")
# plt.ylabel("no of pixels")
# plt.xlabel("Bins")
# colors = ("b", "g", "r")
# for i, col in enumerate(colors):
#     hist = cv.calcHist([resized_img], [i], None, [256], [0, 256])
#     plt.xlim([0, 256])
#     plt.plot(hist, color=col)
# plt.show()

src = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)

clahe = cv.createCLAHE(clipLimit=40)
result = clahe.apply(src)

dst = cv.equalizeHist(src)
cv.imshow("Gray", src)
cv.imshow("equalized histogram", dst)
cv.imshow("result", result)
cv.waitKey(0)
