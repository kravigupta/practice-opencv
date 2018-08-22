# Author: Ravi Kumar Gupta
# Github: https://github.com/kravigupta
# Twitter: https://twitter.com/kravigupta

import cv2

import numpy as np


# haarcascade_frontalface_default.xml

# image taken from https://www.nme.com/news/tv/big-bang-theory-update-eleventh-season-1941471
im = cv2.imread('images/BigBangTheoryGettyImages-503820038.jpg')

grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

haar_face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt_tree.xml')
faces = haar_face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)
print('Faces {}'.format(len(faces)))

for x,y,w,h in faces:
    cv2.rectangle(im, (x,y),(x+w,y+h), (0,255,0), 2)

cv2.imshow('Grey', im)
cv2.imwrite('images/BigBangTheoryGettyImages_face_detected.jpg', im)

cv2.waitKey(0)
cv2.destroyAllWindows()