from this import d
from types import NoneType
import pyautogui
import PIL
from time import sleep
import random

pyautogui.PAUSE = 0.01

keys = {"0": "left", "1": "right", "2": "up", "3": "down"}

def updateKey(key, direction):
    ## Direction == True means up
    if direction:
        pyautogui.keyUp(key)
    else:
        pyautogui.keyDown(key)
    
def click():
    pyautogui.mouseDown();
    pyautogui.mouseUp();

def rightClick():
    pyautogui.mouseDown(button="right");
    pyautogui.mouseUp(button="right");

def checkLocations():
    d = 0.6
    if not (pyautogui.locateCenterOnScreen("human.PNG", confidence=d) is None):
        for i in [pyautogui.locateCenterOnScreen("human.PNG", confidence=d)]:
            pyautogui.moveTo(list(i)[0], list(i)[1])
            click()

if __name__ == "__main__":
    print("Python Surviv IO Bot")
    while True:
       checkLocations()