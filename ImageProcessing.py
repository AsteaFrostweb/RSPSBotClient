import cv2
import numpy as np
import pyautogui
from PIL import Image
import win32gui 
import Debug

def GetScreenShot() -> Image:
    return pyautogui.screenshot()
    
def DoesWindowExist(name) -> bool:
    exists = False
    def callback(hwnd, lParam):
        nonlocal exists
        #Debug.IPLog(win32gui.GetWindowText(hwnd))
        if win32gui.GetWindowText(hwnd) == lParam:
            exists = True

    win32gui.EnumWindows(callback, name)

    return exists


