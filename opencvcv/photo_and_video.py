import cv2
import numpy as np

img = cv2.imread('images/DSCN1637.JPG')

img = cv2.resize(img, (img.shape[1] // 5,img.shape[0] //5))
img = cv2.Canny(img, 200, 200)

kernel = np.ones((5,5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

       # РАБОТА С ФОТО
# img = cv2.GaussianBlur(img, (11, 11), 0) РАЗМЫТИЕ
# new_img = cv2.resize(img,(300, 500)) ИЗМЕНЕНИЕ ЗНЕЧЕНИЙ КАРТИНКИ СНАЧАЛА ШИРИНА ПОТОМ ВЫСОТА
#cv2.imshow('KIRILL LOH', img[0:100, 0:150]) БРЕЗАН7ИЕ ФОТО
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ИЗМЕНЕНИЕ ФОРМАТА
# print(img.shape) сведения о картинке
#img = cv2.Canny(img, 90, 90) НАХОЖДЕНИЕ УГЛОВ КАРТИНКИ
    # kernel = np.ones((5,5), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1) УВЕЛИЧЕНИЕ ОБВОДКИ
    #img = cv2.erode(img, kernel, iterations=1) УМЕНЬШЕНИЕ ОБВОДКИ


cv2.imshow('KIRILL LOH', img)


cv2.waitKey(0)

     #ВИДЕОООО
# cap = cv2.VideoCapture('videos/MVI_0135.mp4')
# cap = cv2.VideoCapture(0) Вебкамера
# cap.set(3, 500) ШИРИНА
# cap.set(4, 300) ВЫСОТА

# while True:
#     success, img = cap.read()
#     cv2.imshow('KIRILL PEDIK', img)
#
#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break

