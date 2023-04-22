import cv2 as cv
from time import sleep


cap = cv.VideoCapture('東方 Bad Apple ＰＶ 影絵.mp4')
img = cv.imread("Apple.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sleep(5)

while cap.isOpened():
    some_thing, frame = cap.read()

    if some_thing is True:
        # img = cv.imread(frame)
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        symbs = ' ⠠⠨⠰⠸⠶⠼⠾⣿'
        scale_multiplier = 6
        ret = ""
        for y in range(0, len(img_gray), scale_multiplier * 2):
            for x in range(0, len(img_gray[y]), scale_multiplier):
                ret += symbs[img_gray[y][x] % len(symbs) - 3]
            ret += '\n'
        print(ret)

        if cv.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
