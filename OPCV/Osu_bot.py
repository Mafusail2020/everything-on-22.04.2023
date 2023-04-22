import cv2 as cv
import pyautogui as pg
from PIL import ImageGrab
import numpy as np


pos = (388, 442)
img = np.array(ImageGrab.grab(bbox=[388, 442, 389, 443]))

img1 = np.array(ImageGrab.grab(bbox=[0, 0, 1000, 1000]))

gray = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
lower = np.array([180, 30, 30])
upper = np.array([208, 100, 100])
mask1 = cv.inRange(img1, lower, upper)

cv.imshow("sus", gray)
cv.imshow("sf", mask1)
cv.waitKey()

gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)

print(mask1[0][0])
