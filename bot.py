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
        for i in range(65):
            click(650, 450)
            time.sleep(0.09)
        x = x - x
        print(x)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
        x += 1
        print(x)
        if x % 60 == 0:
            print(x % 50)
            click(650, 450)

   

