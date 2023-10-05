import cv2
import numpy as np
import pyautogui
from PIL import Image
import win32gui 
import Debug

def GetScreenShot() -> Image:
    return pyautogui.screenshot()
    
def GetHwndByName(name) -> int:
    HWND = 9999
    def callback(hwnd, lParam):
        nonlocal HWND
        #Debug.IPLog(win32gui.GetWindowText(hwnd))
        if win32gui.GetWindowText(hwnd) == lParam:
            HWND = hwnd

        win32gui.EnumWindows(callback, name)

        if(HWND == 9999):
            return None
        else:
            return HWND

def DoesWindowExist(name) -> bool:
    exists = False
    def callback(hwnd, lParam):
        nonlocal exists
        #Debug.IPLog(win32gui.GetWindowText(hwnd))
        if win32gui.GetWindowText(hwnd) == lParam:
            exists = True

    win32gui.EnumWindows(callback, name)

    return exists


