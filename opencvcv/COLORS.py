import cv2
import numpy as np


img = cv2.imread('images/DSCN1637.JPG')
img = cv2.resize(img,(img.shape[1] // 6,img.shape[0] //6))

b,g,r = cv2.split(img)
img = cv2.merge([b,g,r])

cv2.imshow('s', img)
cv2.waitKey(0)


# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) ПЕРЕВОД В HSV
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) ПЕРЕВОД В LAB
# b,g,r = cv2.split(img) РАЗБИЕНИЕ НА ЦВЕТА
# img = cv2.merge([b,g,r]) ОБЪЕДИНЕНИЕ СЛОЕВ
