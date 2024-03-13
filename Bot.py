from enum import Enum

import pyautogui
import pydirectinput
import time

from PIL import Image


def main():
    currentSize = pyautogui.size()
    proportion = (3840/currentSize[0], 2160/currentSize[1])
    originalImage = Image.open('Images/lobby.png')
    newImage = originalImage.resize((originalImage.size[0] * proportion[0], originalImage.size[1] * proportion[1]), Image.Resampling.BICUBIC)
    newImage.save('Images/lobbyresize.png')
    originalImage = Image.open('Images/battleResult.png')
    newImage = originalImage.resize((originalImage.size[0] * proportion[0], originalImage.size[1] * proportion[1]), Image.Resampling.BICUBIC)
    newImage.save('Images/battleResultresize.png')
    originalImage = Image.open('Images/retryQuest.png')
    newImage = originalImage.resize((originalImage.size[0] * proportion[0], originalImage.size[1] * proportion[1]), Image.Resampling.BICUBIC)
    newImage.save('Images/retryQuestresize.png')
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
            battleResult = pyautogui.locateOnScreen('Images/battleResultresize.png', confidence=0.9)
            pydirectinput.press("enter")
        except pyautogui.ImageNotFoundException:
            print("Not in Battle Result")
        for i in range(0, 3):
            pydirectinput.mouseDown(button='left')
            pydirectinput.mouseUp(button='left')


def Lobby():
    print("In Lobby")
    pydirectinput.press("r")
    time.sleep(.25)
    pydirectinput.press("enter")
    time.sleep(.25)
    pydirectinput.press("enter")
    time.sleep(1)
    pydirectinput.press("w",presses=5)
    time.sleep(.25)
    #At this point, we are in the quest counter
    pydirectinput.press("f")
    time.sleep(.25)
    #At this point, we are in the quest selection
    pydirectinput.press("enter")
    time.sleep(.25)
    #At this point, we are 
    pydirectinput.press("enter")
    time.sleep(.25)
    pydirectinput.press("enter")
    time.sleep(.25)
    pydirectinput.press("enter")
    time.sleep(.25)
    pydirectinput.press("enter")
    time.sleep(.25)
    pydirectinput.press("enter")
    #Accepted quest
    time.sleep(2)
    pydirectinput.press("3")
    time.sleep(.25)
    pydirectinput.press("enter")


if __name__ == "__main__":
    main()
