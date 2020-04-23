'''
Doc link: https://pyautogui.readthedocs.io/en/latest/mouse.html

Это простая система для контроля движения мыши.

Для работы с селекторами, XML node и xPath необходимо найти другой модуль.

'''

import pyautogui
import time

# pyautogui.moveTo(690,0,5) # движение

# pyautogui.click(690,0,5) # кнопка

# pyautogui.rightClick # нажатие правой кнопки

# pyautogui.leftClick # нажатие левой кнопки

'''
pyautogui.sleep(1)

pyautogui.typewrite("print('Hello world')")

print('Hello world')

'''

pyautogui.keyDown("shift")
#pyautogui.keyDown()

pyautogui.sleep(1)
pyautogui.keyDown("ctrl")
pyautogui.keyUp("ctrl")
pyautogui.keyUp("shift")
#pyautogui.keyUp()


