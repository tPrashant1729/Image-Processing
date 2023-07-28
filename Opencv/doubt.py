# import cv2 as cv
# import numpy as np

# array = cv.imread('D:\Dnk_project\output\chelsea.png')
# print(type(array))
# cv.imshow('original', array)
# resized= cv.resize(array, (500, 500))
# cv.imshow('static', resized)
# cv.waitKey(0)

# img = cv.imread('D:\Dnk_project\output\chelsea.png')
# cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
# cv.imshow('image', img)
# cv.waitKey()


# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# sobelx = cv.Sobel(grey, cv.CV_32F, 1, 0)
# # find minimum and maximum intensities
# minVal = np.amin(sobelx)
# maxVal = np.amax(sobelx)
# draw = cv.convertScaleAbs(sobelx, alpha=255.0/(maxVal - minVal), beta=-minVal * 255.0/(maxVal - minVal))
# cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
# cv.imshow('image', draw)
# cv.waitKey(0)

# import cv2
# import numpy as np

# # Replace 'path_to_image.jpg' with the path to your image file
# img = cv2.imread('D:\Dnk_project\output\chelsea.png')

# # Define the border size and color
# border_size = 50
# border_color = [0, 255, 0]  # Green color in BGR format

# # Add the border to the image
# bordered_img = cv2.copyMakeBorder(img, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)

# # Resize the original image to match the size of the bordered image
# original_resized = cv2.resize(img, (bordered_img.shape[1], bordered_img.shape[0]))

# # Display the original and bordered images side by side
# combined_image = np.vstack((original_resized, bordered_img))
# cv2.imshow('Original Image vs Bordered Image', combined_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Replace 'path_to_image.jpg' with the path to your image file
img = cv2.imread("D:\Dnk_project\output\chelsea.png", cv2.IMREAD_GRAYSCALE)
# img = cv2.medianBlur(img, 3)
# # Apply the Sobel operator
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in x-direction
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in y-direction

# # Calculate the magnitude and direction of the gradient
# gradient_magnitude = np.sqrt(sobelx**2 + sobely**2)
# gradient_direction = np.arctan2(sobely, sobelx)

# # Threshold the gradient magnitude to obtain edges
# threshold_value = 100
# edges = np.zeros_like(gradient_magnitude)
# edges[gradient_magnitude > threshold_value] = 255

# # Display the original image and the edges
# cv2.imshow('Original Image', img)
# cv2.imshow('Edges', edges.astype(np.uint8))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

# Assuming you have already loaded 'img' using cv2.imread() or some other method

# Step 1: Apply blur to reduce noise in the image
img_blurred = cv2.blur(img, (3, 3))

# Step 2: Apply Canny edge detection to find edges in the image
edges = cv2.Canny(img_blurred, 100, 150)

# Step 3: Find contours in the edge-detected image
# The 'contours' variable will store a list of contours, and 'i' is not needed here.
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 4: Draw the convex hull on a copy of the original image
img_with_convex_hull = np.zeros((img.shape[0], img.shape[1]), np.uint8)

# Step 5: Find the convex hull of the contours
# We need to specify which contour to use for finding the convex hull. In this case, I'm using the third contour (index 2).
for i in range(len(contours)):
    convex_hull = cv2.convexHull(contours[i])
    cv2.drawContours(
        img_with_convex_hull, [convex_hull], -1, (255, 255, 255), thickness=cv2.FILLED
    )

print(len(contours))
# Step 6: Display the resulting image
cv2.imshow("convex_hull", img_with_convex_hull)
cv2.waitKey(0)
cv2.destroyAllWindows()
