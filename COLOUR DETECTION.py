import cv2
import numpy as np

# COLOUR DETECTION
# pixel to pixel comparison is what happens in COLOUR DETECTION
img = cv2.imread('./pictures/1997.jpg')

# we will be looking for another color scheme known as hsv and it is used in color and paint software
# first convert to hsv format before colour detection
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# then write upper and lower limits(radius) of each colour eg green has a lower and upper limit of [40, 40,
# 40] and [70. 255, 255] respectively...
lower_blue = np.array([0, 50, 50])
upper_blue = np.array([140, 255, 255])

# threshold the HSV image to get only blue colors
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img, img, mask = mask_blue)
cv2.imshow('IMAGE', res)


cv2.waitKey(0)
cv2.destroyAllWindows()
