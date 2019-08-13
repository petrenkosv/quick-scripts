from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time

class Cordinates():
    replayBtn = (342,389)
    dinasaur = (164,394)
    #240=x cordinates to check the tree
    #y cordinate = 374

def restartGame():
    pyautogui.doubleClick(Cordinates.replayBtn)
    pyautogui.keyDown('space')
    time.sleep(0.2)
    print("Start")
    pyautogui.keyUp('space')
    
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.15)
    print("Jump")
    pyautogui.keyUp('space')
    

def pressDown():
    pyautogui.keyUp('down')
    time.sleep(0.18)
    print("Duck")
    pyautogui.keyDown('down')

def imageGrab():
    box = (
        Cordinates.dinasaur[0]+89,
        Cordinates.dinasaur[1],
        Cordinates.dinasaur[0]+134,
        Cordinates.dinasaur[1]+30
        )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print (a.sum())
    return a.sum()

    
def main():
    restartGame()
    while True:
        if(imageGrab() != 1597):
            pressSpace()
            time.sleep(0.1)
    
main()