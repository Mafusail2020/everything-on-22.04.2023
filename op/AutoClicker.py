import pyautogui as pg
import keyboard
from threading import Thread


def to_click():
    for _ in range(10):
        pg.click()


threads = []
for _ in range(100):
    threads.append(Thread(target=to_click))

while True:

    if keyboard.is_pressed('f'):
        for thread in threads:
            thread.start()
