from enum import Enum

import cv2
import pyautogui
import pydirectinput
import time

from PIL import Image


def main():
    currentSize = pyautogui.size()
    proportion = (currentSize[0]/3840, currentSize[1]/2160)
    originalImage = cv2.imread('Images/lobby.png')
    newImage = cv2.resize(originalImage, (0, 0), fx=proportion[0], fy=proportion[1])
    cv2.imwrite('Images/lobbyresize.png', newImage)
    originalImage = cv2.imread('Images/battleResult.png')
    newImage = cv2.resize(originalImage, (0, 0), fx=proportion[0], fy=proportion[1])
    cv2.imwrite('Images/battleResultresize.png', newImage)
    originalImage = cv2.imread('Images/retryQuest.png')
    newImage = cv2.resize(originalImage, (0, 0), fx=proportion[0], fy=proportion[1])
    cv2.imwrite('Images/retryQuestresize.png', newImage)
    print("Waiting 10 seconds")
    time.sleep(10)
    while True:
        try:
            lobby = pyautogui.locateOnScreen('Images/lobbyresize.png', confidence=0.6)
            Lobby()
        except pyautogui.ImageNotFoundException:
            print("Not in Lobby")
        try:
            retry = pyautogui.locateOnScreen('Images/retryQuestresize.png', confidence=0.6)
            pydirectinput.press("3")
            time.sleep(.25)
            pydirectinput.press("enter")
        except pyautogui.ImageNotFoundException:
            print("Don't need to retry")
        try:
            battleResult = pyautogui.locateOnScreen('Images/battleResultresize.png', confidence=0.6)
            pydirectinput.press("enter")
        except pyautogui.ImageNotFoundException:
            print("Not in Battle Result")
        for i in range(0, 3):
            pydirectinput.mouseDown(button='left')
            pydirectinput.mouseUp(button='left')


def Lobby():
    print("In Lobby")
    pydirectinput.press("r")
    time.sleep(.5)
    pydirectinput.press("enter")
    time.sleep(.5)
    pydirectinput.press("enter")
    time.sleep(1)
    pydirectinput.press("w",presses=5)
    time.sleep(.5)
    #At this point, we are in the quest counter
    pydirectinput.press("f")
    time.sleep(.5)
    #At this point, we are in the quest selection
    pydirectinput.press("enter")
    time.sleep(.5)
    #At this point, we are 
    pydirectinput.press("enter")
    time.sleep(.5)
    pydirectinput.press("enter")
    time.sleep(.5)
    pydirectinput.press("enter")
    time.sleep(.5)
    pydirectinput.press("enter")
    time.sleep(.5)
    pydirectinput.press("enter")
    #Accepted quest
    time.sleep(2)
    pydirectinput.press("3")
    time.sleep(.5)
    pydirectinput.press("enter")


if __name__ == "__main__":
    main()
