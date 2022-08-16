
import cv2 as cv
import numpy as np

img = cv.imread("image/flag.jpg")
#print original image
print(img.shape)
cv.imshow('My Image',img)

# # Grayscaling and Thresholding image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)



cv.imshow('My Image',img)
cv.waitKey(0)
cv.destroyAllWindows()