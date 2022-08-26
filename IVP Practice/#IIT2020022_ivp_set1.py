#IIT2020022_ivp_set1.py

from PIL import Image
import scipy.ndimage
import numpy as np
import cv2 as cv


im = Image.open('/exp1.png')
cv.imshow(im)
data = im.getdata()
r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]
im.putdata(r)
cv.imshow(im)
im.putdata(g)
cv.imshow(im)
im.putdata(b)
cv.imshow(im)