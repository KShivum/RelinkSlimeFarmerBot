from enum import Enum

import pyautogui
import pydirectinput
import time

def main():
    while True:
        try:
            lobby = pyautogui.locateOnScreen('Images/lobby.png', confidence=0.6)
            Lobby()
        except pyautogui.ImageNotFoundException:
            print("Not in Lobby")
        try:
            retry = pyautogui.locateOnScreen('Images/retryQuest.png', confidence=0.6)
            pydirectinput.press("3")
            time.sleep(.25)
            pydirectinput.press("enter")
        except pyautogui.ImageNotFoundException:
            print("Don't need to retry")
        try:
            battleResult = pyautogui.locateOnScreen('Images/battleResult.png', confidence=0.9)
            pydirectinput.press("enter")
        except pyautogui.ImageNotFoundException:
            print("Not in Battle Result")
        for i in range(0, 3):
            pydirectinput.mouseDown(button='left')
            pydirectinput.mouseUp(button='left')


def BattleResult():
    try:
        while True:
            battleResult = pyautogui.locateOnScreen('Images/battleResultPart1.png', confidence=0.7)
            pyautogui.click(clicks=2, interval=0.5)
    except pyautogui.ImageNotFoundException:
        print("Not in Battle Result part 1")
    try:
        battleResult = pyautogui.locateOnScreen('Images/retryQuest.png', confidence=0.7)
        pyautogui.press("3")
        pyautogui.press("enter")
    except pyautogui.ImageNotFoundException:
        print("Don't need to retry")
    pyautogui.press("enter")
    pyautogui.press("enter")

def GetCurrentState():
    try:
        lobby = pyautogui.locateOnScreen('Images/lobby.png', confidence=0.5)
        Lobby()
    except pyautogui.ImageNotFoundException:
        print("Not in Lobby")
    try:
        battleResult = pyautogui.locateOnScreen('Images/battleResult.png', confidence=0.9)
        return GameState.BattleResult
    except pyautogui.ImageNotFoundException:
        print("Not in Battle Result")
    
    return GameState.Other

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


class GameState(Enum):
    Lobby = 1
    BattleResult = 2
    Other = 3
