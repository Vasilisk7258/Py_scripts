import cv2
import numpy as np

photo = cv2.imread('images/DSCN1637.JPG')
photo = cv2.resize(photo,(photo.shape[1] // 6,photo.shape[0] //6))

new_img = np.zeros((photo.shape[:2]), dtype='uint8')

circle = cv2.circle(new_img.copy(), (0,0), 80, (255, 255, 255), -1)
square = cv2.rectangle(new_img.copy(), (25, 25), (250,350), 255, -1)

new_img = cv2.bitwise_and(photo, photo, mask=square)

cv2.imshow('s', new_img)
cv2.waitKey(0)


# new_img = cv2.bitwise_and(circle, square) НАХОДИТ ОДИНАКОВОЕ
# new_img = cv2.bitwise_or(circle, square) ВСЕ ОБЪЕДИНЯЕТ
# new_img = cv2.bitwise_xor(circle, square) ВСЕ РАЗНОЕ НА ОДНОЙ ФОТКЕ
# new_img = cv2.bitwise_not(circle) ИНВЕРСИЯ
# new_img = cv2.bitwise_and(photo, photo, mask=circle) ИСПОЛЬЗОВАНИЕ МАСКИ