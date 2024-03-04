import cv2
import numpy as np

photo = np.zeros((300,300, 3), dtype='uint8')



cv2.rectangle(photo, (3, 3), (100, 100), (180,30,210), thickness=3)

cv2.line(photo, (20,20), (30,30), (180,30,210), thickness=20)

cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 25, (180,30,210), thickness=cv2.FILLED)

cv2.putText(photo, 'HUUUUI', (10,250), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0), thickness=2)

cv2.imshow('asdasd', photo)
cv2.waitKey(0)


# photo[100:200, 200:300] = 180,30,210 ЗАКРАСКА ОБЛАСТИ ФОТО НАЧИНАЯ С ВЫСОТЫ
# cv2.rectangle(photo, (3, 3), (100, 100), (180,30,210), thickness=3) СОЗДАЕТ КВАДРАТ НАЧИНАЯ С 3 3 И ДО 100 100 ТОЛЩИНОЙ 3
                                                                # =cv2.FILLED ЗАЛИВКА
# cv2.line(photo, (20,20), (30,30), (180,30,210), thickness=20) ЛИНИЯ ВСЕ ТАК ЖЕ КАК У КВАДРАТА
# cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 25, (180,30,210), thickness=cv2.FILLED) КРУУУУГ
# cv2.putText(photo, 'HUUUUI', (10,250), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0), thickness=2)
# ТЕКСТ НАЧАЛЬНАЯ ТОЧКА ШРИФТ РАЗМЕР ЦВЕТ И ТОЛЩИНА