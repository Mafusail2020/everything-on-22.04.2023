from threading import *
from time import sleep


def bruh(r):
    while True:
        print(r)
        sleep(1)


t1 = Thread(target=bruh, args=("#",))
t1.start()

input("Enter a number")

