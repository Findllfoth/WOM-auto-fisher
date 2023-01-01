# WOM-auto-fisher
This is a fishing bot that uses python to fish for you 

All the things you need to paste into the command prompt

pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
pip install Pillow

Code to copy into to python after download

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse 

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

x = 0
while 1:
    if pyautogui.locateOnScreen('mark2.png', confidence=0.5) !=None:
# i is used for how many clicks are used
        for i in range(65):
            click(650, 450)
            time.sleep(0.09)
# this expression resets the counter so you are not having a line casted out then the code brings it back in
        x = x - x
        print(x)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
        x += 1
        print(x)
# This if statement is two things a counter and to help cast out the line if a fish has not been caught in a set time 
        if x % 60 == 0:
            print(x % 50)
            click(650, 450)

   

