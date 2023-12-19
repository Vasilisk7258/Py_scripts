# библиотеки
import pyautogui
import keyboard

#функция нажатия
def click(x,y):
    pyautogui.click(x, y)


while not keyboard.is_pressed('q'):
    # проверка пикселя на то, черный он или нет
    if pyautogui.pixel(625,688)[0] == 0:
        click(625,700)
    if pyautogui.pixel(784, 688)[0] == 0:
        click(784,700)
    if pyautogui.pixel(907, 688)[0] == 0:
        click(907,700)
    if pyautogui.pixel(1057, 688)[0] == 0:
        click(1057,700)











