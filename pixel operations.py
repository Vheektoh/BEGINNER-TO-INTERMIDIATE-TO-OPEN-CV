import cv2
import numpy as np
# accessing pixel values and modifying them
img = cv2.imread('./pictures/1997.jpg')
px = img[100, 100]
print(px)
# the BGR value of the pixel above[100,100] is  [165 195 222], so on the image,
# the pixel position 100, 100 is the above
# accessing the blue pixel
blue = img[100, 100, 0]
print(blue)
# modifying the pixel values
img[100, 100] = [255, 255, 255]

# image properties
############################################################
img_file = './pictures/1997.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR) # rgb image
alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # alpha image
gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE) # greyscale image
# printing the image.shape shows the rows, columns and channels of each kind of image filter above
# image.dtype gives the data type
# image.size also gives the size
############################################################
# SETTING THE REGION OF THE IMAGE ie selecting certain cropped parts of image
img_file2 = './pictures/finey.jpeg'
img_raw = cv2.imread(img_file2)

roi = cv2.selectROI(img_raw)

# CROPPING selected region of image from the raw(given)  image
roi_cropped = img_raw[int(roi[1]) : int(roi[1] + roi[3]), int(roi[0]) : int(roi[0] + roi[2])]
cv2.imshow('ROI image', roi_cropped)
cv2.imwrite('cropped.jpeg', roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# SPLITTING AND MERGING IMAGES
img_f = './pictures/cropped.jpeg'
img_2 = cv2.imread(img_f)

b, g, r = cv2.split(img_2)
cv2.imshow('blue part of the image', b)
cv2.imshow('green part of the image', g)
cv2.imshow('red part of the image', r)

# merging the above into existing image to get the original image
img_m = cv2.merge((b, g, r))
cv2.imshow('merged image of 3 colors', img_m)

cv2.waitKey(0)

# CHANGING COLOR OF IMAGE to other aspects apart from bgr etc
colour_change = cv2.cvtColor(img_2, cv2.COLOR_RGB2LAB)
cv2.imshow('changed color scheme image', colour_change)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Blend two different images
# first image
src1 = cv2.imread('./pictures/finey.jpeg', cv2.IMREAD_COLOR)
# second image
src2 = cv2.imread('./pictures/1997.jpg', cv2.IMREAD_COLOR)
# images should be the same size
img1 = cv2.resize(src1, (800, 600))
img2 = cv2.resize(src2, (800, 600))
# blending
blended_img = cv2.addWeighted(img1, 1, img2, 0.7, 1.0)
cv2.imshow("blended image", blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# APPLYING FILTERS ON IMAGES
image = cv2.imread('./pictures/finey.jpeg')
# make an array for the kernel when applying filters
k_sharped  = np.array([[-2, -2, -3],
                       [-2, 22, -4],
                       [-2, -3, -2]])
sharpened = cv2.filter2D(image, -1, k_sharped)

cv2.imshow('filtered image', sharpened)
cv2.imshow('original image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGE THRESHOLDING - FINDING EDGES IN EDGES
# always convert images to greyscale before preprocessing for space complexity problems
# canny edge detector is one of the most used
image = cv2.imread('./pictures/finey.jpeg', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
canny_image = cv2.Canny(image, 50, 100)

cv2.imshow('original image', image)
cv2.imshow('threshold image', thresh)
cv2.imshow('canny image', canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


