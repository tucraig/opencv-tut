import cv2
import numpy as np
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("test.jpg")
gray = cv2.imread("test.jpg",cv2.IMREAD_GRAYSCALE)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imwrite('output.jpg',img)
