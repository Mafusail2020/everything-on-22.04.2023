import cv2 as cv

img = cv.imread("Bruuuh.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

converted_img = cv.imread("ASCII_file_pattern.png")

# cv.resize(converted_img, dsize=(len(img_gray[0]), len(img_gray)))
# cv.resize(converted_img, dsize=(img_gray.shape[1], img_gray.shape[0]), interpolation=cv.INTER_AREA)
small_mult = 1
if True:
    symbs = ' ixzao*#MW&8%B@$'
    for y in range(0, len(img_gray), small_mult):
        for x in range(0, len(img_gray[y]), small_mult):
            print(symbs[(img_gray[y][x] // len(symbs))*-1-1]*2, end="")
            cv.putText(converted_img,
                       text=symbs[(img_gray[y][x] // len(symbs))*-1-1]*1,
                       org=(10*(x+1), 12*(y+1)), # May be an error here
                       fontFace=cv.FONT_HERSHEY_SIMPLEX,
                       fontScale=0.5,
                       color=(0, 0, 0, 0),
                       thickness=1)
        print()

# cv.imshow("Phew", converted_img)
cv.imwrite("ASCII compilied.png", converted_img)
cv.waitKey(0)
