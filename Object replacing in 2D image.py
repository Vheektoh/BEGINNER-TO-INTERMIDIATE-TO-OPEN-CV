import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./pictures/ghoul.jpg', cv2.IMREAD_COLOR)

# create copy image of img above
img1 = img.copy()
mask = np.zeros((100, 300, 3))

pos = (200, 200)
var = img1[200 : (200 + mask.shape[0]), 200: (200 + mask.shape[1])] = mask
cv2. imshow('replaced image', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()