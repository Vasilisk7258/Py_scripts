import cv2
import numpy as np



img = cv2.imread('images/DSCN1637.JPG')


img = cv2.resize(img,(img.shape[1] // 6,img.shape[0] //6))
new_img = np.zeros(img.shape, dtype='uint8')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (120,0,0), 1)

cv2.imshow('s', new_img)
cv2.waitKey(0)

# img = cv2.flip(img, 0) ОТЗЕРКАЛИВАНИЕ 0 ПО ВЕРТИКАЛИ 1 ПО ГОРИЗОНТАЛИ -1 ПО ВСЕМ ОСЯМ


# def rotate(image, angel): ФУНКЦИЯ ПО ВРАЩЕНИЮ
#     height, weigtht = img.shape[:2]    ВЫСОТА И ШИРИНА
#     point = (weigtht // 2, height // 2)    ЦЕНТР
#
#     mat = cv2.getRotationMatrix2D(point, angel, 1)  МАТРИЦА ЧТОБЫ ПОВЕРНУТЬ
#     return cv2.warpAffine(image, mat, (weigtht, height)) ВОЗВРАЩАЕМ ТО ЧТО НАДО
#
#
# img = rotate(img, 20)
# def transform(_img, x,y):    ФУНКЦИЯ СМЕЩЕНИЯ
#     mat = np.float32([[1, 0, x], [0,1,y]])    МАТРИЦА
#     return cv2.warpAffine(_img, mat, (_img.shape[1], _img.shape[0])) ВОЗВРАЩАЕМ ТО ЧТО НАДО
#
# img = transform(img, 10,20)

# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) НАХОДИМ КОНТУРЫ
# cv2.drawContours(new_img, con, -1, (120,0,0), 1) РИСУЕМ КАРТИНКУ ПО КОНТУРАМ

