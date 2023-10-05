import win32api 
import pyautogui

def main():
    while(True):
        if win32api.GetAsyncKeyState(ord('A')) & 0x8000:
            print("Mouse Pos: " + str(pyautogui.position()))

if __name__ == "__main__":
    main()

def Log(s):
    print(s)

def BMLog(s):
    print("[BotManager] " + s)

def IPLog(s):
    print("[ImageProcessing] " + s)
    