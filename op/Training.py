import pyautogui as pg
import time
from random import randint
import keyboard
# pg.moveTo(x, y, duration=a)
# pg.click(x, y, duration=a)
# pg.hotley("key1", "key2")
# pg.typewrite("txt", duration=x)

# print(pg.position())
print("Нажми на F чтобы напечатать 100 сообщений (Сначала выделии строку ввода в чате)")

is_enabled = False
while True:
    if keyboard.is_pressed("f"):
        is_enabled = True

    if is_enabled:
        for i in range(100):
            pg.hotkey("ctrlleft", 'v')
            keyboard.press("enter")
            if keyboard.is_pressed("g"):
                is_enabled = False
            time.sleep(randint(0, 5)/10)
    is_enabled = False
