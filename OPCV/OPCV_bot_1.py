import cv2 as cv
import pyautogui as pg
import numpy as np
from PIL import ImageGrab


mouse_pos = pg.position()
# Previos grab
# grab = [mouse_pos.x-100, mouse_pos.y-100, mouse_pos.x+100, mouse_pos.y+100]
grab = [mouse_pos.x-10, mouse_pos.y+10, mouse_pos.x+10, mouse_pos.y+10]
area = np.array(ImageGrab.grab(bbox=grab))
area = cv.cvtColor(area, cv.COLOR_BGR2HSV)

# From darker to brighter
lower_red = np.array([0, 50, 50])
upper_red = np.array([6, 255, 255])
mask = cv.inRange(area, lower_red, upper_red)


lower_aqua = np.array([170, 50, 50])
upper_aqua = np.array([180, 255, 255])
mask1 = cv.inRange(area, lower_aqua, upper_aqua)

# cv.imshow("ZA CHTO!?!?!?", mask + mask1)
# cv.waitKey()
print(mask)
if np.sum(mask) > 1:
    print("RED")
else:
    pass

# print("Red is spotted" if np.sum(4) > 1 else "Red is not spotted")
# is_red(area)
# cv.imshow("Area", area)
# cv.waitKey()
