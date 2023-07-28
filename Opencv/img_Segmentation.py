from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

rng.seed(12345)
parser = argparse.ArgumentParser(
    description="Code for Image Segmentation with Distance Transform and Watershed Algorithm.\
 Sample code showing how to segment overlapping objects using Laplacian filtering, \
 in addition to Watershed and Distance Transformation"
)
parser.add_argument(
    "--input",
    help="Path to input image.",
    default=r"D:\Dnk_project\output\astronaut.png",
)
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print("Could not open or find the image:", args.input)
    exit(0)
# Show source image
cv.imshow("Source Image", src)
src[np.all(src == 255, axis=2)] = 0
# Show output image
cv.imshow("Black Background Image", src)
kernel = np.array([[1, 1, 1], [1, -9, 1], [1, 1, 1]], dtype=np.float32)
# do the laplacian filtering as it is
# well, we need to convert everything in something more deeper then CV_8U
# because the kernel has some negative values,
# and we can expect in general to have a Laplacian image with negative values
# BUT a 8bits unsigned int (the one we are working with) can contain values from 0 to 255
# so the possible negative number will be truncated
imgLaplacian = cv.filter2D(src, cv.CV_32F, kernel)
sharp = np.float32(src)
imgResult = sharp - imgLaplacian
cv.imshow("New Sharped Image 1st", imgResult)

# convert back to 8bits gray scale
imgResult = np.clip(imgResult, 0, 255)
imgResult = imgResult.astype("uint8")
imgLaplacian = np.clip(imgLaplacian, 0, 255)
imgLaplacian = np.uint8(imgLaplacian)
# cv.imshow('Laplace Filtered Image', imgLaplacian)
cv.imshow("New Sharped Image", imgResult)
cv.imshow("New Sharped Image laplacian", imgLaplacian)

cv.waitKey(0)
