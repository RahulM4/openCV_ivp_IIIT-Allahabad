
import time
import cv2 as cv
import numpy as np
import PIL as pil

img = cv.imread("image/flag.jpg")
# #print original image
print(img.shape)
cv.imshow('My Image',img)

# # Grayscaling and Thresholding image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)
cv.imwrite('image/gray.jpg',gray)


# Crop the Image 
crop_img = img[0:200, 0:200]
cv.imshow('Crop Image',crop_img)
cv.imwrite('image/crop_img.jpg',crop_img)



# # resize Image and save into new file
resized_img = cv.resize(img, (200, 200))
cv.imshow('Resized Image',resized_img)
cv.imwrite('image/resized_flag.jpg',resized_img)





# # image rotaion and save  into new file
M = cv.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 90, 1)
rotated_img = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv.imshow('Rotated Image',rotated_img)
cv.imwrite('image/rotated_flag.jpg',rotated_img)


# Blurring Smoothing image
blurImg = cv.blur(img, (10, 10))
cv.imshow('Blurred Image', blurImg)



cv.waitKey(0)
cv.destroyAllWindows()