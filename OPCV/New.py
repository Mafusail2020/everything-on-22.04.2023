import numpy as np
import cv2 as cv

img = cv.imread("image.png")
HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

up = np.array([235, 255, 255])
low = np.array([90, 255, 232])
mask = cv.inRange(HSV, low, up)

print(HSV[110][110])
cv.imshow("No.", mask)
cv.waitKey()
