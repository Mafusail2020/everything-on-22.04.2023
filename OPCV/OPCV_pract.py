import cv2 as cv

img = cv.imread("Woman.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
print(f"Faces detected: {len(faces)}")
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv.imshow(f"{len(faces)} faces detected", img)
cv.waitKey()
