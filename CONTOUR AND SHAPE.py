import cv2
import numpy as np
import matplotlib.pyplot as plt

# CONTOUR AND SHAPE DETECTION
# outer body part or boundary detection
img = cv2.imread('./pictures/shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# SETTING THRESHOLD OF GRAY SCALE IMAGE
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# FINDING CONTOURS
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# retrieve the outer boundaries in image and approx simple is used to finding the connection in chain in an
# image...pixel to pixel

i = 0
for contour in contours:
    if i == 0:
        i = 1
        continue
    appox = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (255, 0, 255), 5)

# finding the center of different shapes
M = cv2.moments(contour)
if M['m00'] != 0.0:
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])

# putting corresponding names inside the corresponding shapes
if len(appox) == 3:
    cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
elif len(appox) == 4:
    cv2.putText(img, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
elif len(appox) == 5:
    cv2.putText(img, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
elif len(appox) == 6:
    cv2.putText(img, 'Hexagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
else:
    cv2.putText(img, 'circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

# displaying things
cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
