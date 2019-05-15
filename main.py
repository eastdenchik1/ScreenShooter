

import os
from datetime import datetime
import pyautogui
import numpy as np 
import imutils 
import cv2
import sys
import msvcrt


def generateScreenshotPath():
    SCREENSHOT_FOLDER = os.getenv('SCREENSHOT_FOLDER', '.temp')
    _datetime = datetime.now()
    dateTimeStr = _datetime.strftime('%Y%m%d%H%M')
    path = SCREENSHOT_FOLDER+'\\'+'screen_{}.jpg'.format(dateTimeStr)
    return path

def createFullscreenShot(path):
    imgPath = path
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    if cv2.imwrite(imgPath, image):
        print(imgPath)
        print('Screenshot has been taken')

def createPartofWindows(path):
    imgPath = path
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    showCrosshair = False
    fromCenter = False
    r = cv2.selectROI("Image", image, fromCenter, showCrosshair)

    imCrop = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    # cv2.imshow("Image", imCrop)
    if cv2.imwrite(imgPath, imCrop):
        print(imgPath)
        print('Screenshot has been taken')


if __name__=='__main__':
    path = generateScreenshotPath()
    # if sys.argv[1]=='-p':
    #     createPartofWindows(path)
    # elif sys.argv[1]=='-f':
    #     createFullscreenShot(path)  
    while True:
        key = msvcrt.getch().lower()

        if key == b'f':
            createFullscreenShot(path)  
        elif key == b'p':
            createPartofWindows(path)
        elif key == b'q':
            print("Quitting...")
            break
        else:
            print(key)