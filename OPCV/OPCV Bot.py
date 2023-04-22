import time

import cv2 as cv
from PIL import ImageGrab
import numpy as np
import pyautogui as pg
import keyboard
area_to_scan = [455, 485, 988, 746]


def i_hate_niggers_really_much(scr):
    global area_to_scan

    for y in range(0, len(scr), 10):
        for x in range(0, len(scr[y]), 10):
            if scr[y][x] < 10 and True:
                real_x = x + area_to_scan[0]
                real_y = y + area_to_scan[1]
                pg.doubleClick(real_x, real_y)
                pg.doubleClick(real_x, real_y)
                return

    scre = np.array(ImageGrab.grab(bbox=[454, 164, 455, 165]))
    scre = cv.cvtColor(scre, cv.COLOR_BGR2GRAY)
    for y1 in range(len(scre)):
        for x1 in range(len(scre[y1])):
            if scre[y1][x1] >= 190:
                time.sleep(1)
                keyboard.press('space')


while True:
    mouse_pos_x, mouse_pos_y = pg.position()

    if area_to_scan[0] - 100 < mouse_pos_x < area_to_scan[2] and area_to_scan[1] < mouse_pos_y < area_to_scan[3]:
        screen = np.array(ImageGrab.grab(bbox=area_to_scan))
        screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)
        # cv.imshow("gasd", screen)
        i_hate_niggers_really_much(screen)

        # cv.waitKey()
