import cv2
from datetime import datetime
from dateutil.relativedelta import relativedelta
from PIL import Image, ImageFont, ImageDraw

user_name = 'sdasdssdsпрgfzxcjkyt'
user_surname = 'asdsadasdwwwфыtttttt'
user_sex = 'МУЖ.'
user_age = 40

date_of_birth = datetime.strftime(datetime.now() - relativedelta(years=user_age), '%Y-%m-%d')
img = Image.open('pass.png')
img2 = Image.open('set814237754.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('comici.ttf', 40)
draw.text((570,210), user_surname, (0,0,0), font=font)
draw.text((520,280), user_name, (0,0,0), font=font)
draw.text((500,333), user_sex, (0,0,0), font=font)
draw.text((560,390), date_of_birth, (0,0,0), font=font)
img2 = img2.crop((420, 200, 870, 720))
img.paste(img2, (30,156), mask=img2)
img.save("papa.png")
# cv2.imshow('sdsdfsdsdff',img2)
# cv2.waitKey(0)
# print(img.shape)
# img2 = img2[350:700, 450:800]
# img2 = cv2.resize(img2, (img2.shape[0]*7//6, img2.shape[1]*7//6))
# print(img2.shape)
# cv2.putText(img, user_surname, (570,250), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), thickness=2)
# cv2.putText(img, user_name, (520,325), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), thickness=2)
# cv2.putText(img, user_sex, (510,380), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), thickness=2)
# cv2.putText(img, date_of_birth, (560,440), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), thickness=2)
# img[267:267+img2.shape[0], 1:1+img2.shape[1]] = img2
# cv2.imwrite('passssss.PNG', img)
