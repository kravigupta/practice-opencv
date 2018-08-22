# Author: Ravi Kumar Gupta
# Github: https://github.com/kravigupta
# Twitter: https://twitter.com/kravigupta

import cv2

import numpy as np


face_det = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt_tree.xml')
eye_det = cv2.CascadeClassifier('cascade/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    img = cv2.flip(frame, 1, 0)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_det.detectMultiScale(grey)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = grey[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_det.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)
    imW, imH, xxx = img.shape
    # print(img.shape)
    # img = cv2.resize(img, ( int(imH/2), int(imW/2)) )
    cv2.imshow('img', img)
    k = cv2.waitKey(20) & 0xff
    if k == 27:
        break
cap.release()

cv2.destroyAllWindows()