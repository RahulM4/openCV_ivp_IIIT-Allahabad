import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter


img = Image.open('image/flag.jpg')
grayIMage = img.convert('L')
IMG =grayIMage.filter(ImageFilter.FIND_EDGES)

IMG.show()

image =cv.imread('image/flag.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

edgeDetection = cv.Canny(gray, 100, 200)
cv.imwrite('image/edge_detection.jpg',edgeDetection)

# Default to Show Promt Message
cv.waitKey(0)
cv.destroyAllWindows()
