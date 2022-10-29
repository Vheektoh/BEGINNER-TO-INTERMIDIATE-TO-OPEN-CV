import cv2
import numpy as np

# reading an image on opencv
image_path = r'./pictures/sharingan_.jpg'
image = cv2.imread(image_path)

# displaying the image
cv2.imshow('sample', image)

# saving an image
directory = r'C:\Users\personal\Pictures'
file_name = 'savedImage.jpg'
cv2.imwrite(file_name, image)
# print("saved successfully")

# accessing image properties
print(image.shape)  # to show image data like number of pixels which outputs(800, 1280, 3) as the rows, columns and
# color channels respectively

# changing the colour space like from gray to RGB and vise versa
# BGR to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original image", image)
cv2.imshow('gray image', gray)
# Gray to BGR will be the reverse of above

# Resizing the image
resize = cv2.resize(image, (50, 50))
cv2.imshow("original image", image)
cv2.imshow('resized image', gray)

# Displaying text on image, opencv comes with 8 diff fonts
# opencv reads RGB as BGR
text = 'Subarashi OpenCv'
coordinates = (150, 100)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
color = (255, 20, 20)
thickness = 2

image = cv2.putText(image, text, coordinates, font, fontscale, color, thickness)
cv2.imshow("original image", image)

# Drawing Objects
# Line...starting and ending points in x and y coordinates, thickness, color etc
start_point = (0, 0)
end_point = (250, 250)
color = (255, 20, 20)
thickness = 2
image = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow('line image', image)

# circle...start from centre point, then radius, then color and thickness
centre_point = (500, 500)
color = (255, 20, 20)
thickness = 2
radius = 100
image = cv2.circle(image, centre_point, radius, color, thickness)
cv2.imshow('circle image', image)

# rectangle... start and end co-ords, color, thickness
starting_p = (120, 50)
ending_p = (250, 250)
color = (255, 20, 20)
thickness = 2
image = cv2.rectangle(image, starting_p, ending_p, color, thickness)
cv2.imshow('rectangle image', image)

# ellipse...starting point, axes length, starting and ending angle, colour and thickness
color = (255, 20, 20)
thickness = 2
centre_coords = (120, 100)
axes_lenght = (100, 50)
angle = 30
start_angle = 0
end_angle = 360
image = cv2.ellipse(image, centre_coords, axes_lenght, angle, start_angle, end_angle, thickness)
cv2.imshow('ellipse image', image)

# single parts of a video are called frames
# adding 0 gives a greyscale image
# adding 1 gives a BGR image
# adding -1 gives original image
img = cv2.imread('./pictures/1997.jpg', 0)
cv2.imshow('original image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
