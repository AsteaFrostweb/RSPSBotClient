import subprocess
import sys
import time
import ImageProcessing as IP
import Debug
import win32con
import win32gui
import pyautogui
import cv2
import numpy as np

launcherWindowTitle = "BlissScape 718"
maxWaitTime = 15.0
hasLauncher = True


def main():
    
    #checking if the command line argument for the botclient jar has been entered
    if(sys.argv[1] == ""):
        Debug.BMLog("Please edit run.bat to include the RSPS jar filename. Example: python BotManager.py [filename].jar")
        return
    

 
   

    if(hasLauncher):
        Debug.BMLog("Initializing " + launcherWindowTitle + " Launcher")
        process = subprocess.Popen("java -jar " + sys.argv[1])    
        time.sleep(2)
        if(process.returncode != None):
            Debug.BMLog("Couldnt locate jar file or java isnt installed")
            return       


        launcherHWND = None
        #waiting till maxWaitTime for the windows to open
        startTime = time.time()
        elapsedTime = time.time() - startTime
        launched = False
        while(elapsedTime <= maxWaitTime):
           
            if(IP.DoesWindowExist(launcherWindowTitle)):                
                launcherHWND = win32gui.FindWindow(None, launcherWindowTitle)
                Debug.BMLog("Launcher Opened " + str(launcherHWND))
                launched = True
                break
            else:
                Debug.BMLog("Waiting for laucher. Elapsed time: " + str(int(elapsedTime)))
            elapsedTime = time.time() - startTime
            time.sleep(1)

        if(launched == False):
            Debug.BMLog("Launcher didn't start in maximum alloted time. Ending program")
            return
        
        win32gui.SetActiveWindow(launcherHWND)
        flags = win32con.SWP_NOSIZE | win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE
        win32gui.SetWindowPos(launcherHWND, None, 0, 0, 0, 0, flags)
        pyautogui.click(300,330)
        


    else:
            Debug.BMLog("Initializing RSPS Client")
            #Attempting to run the .jar through the command line with args[1] from the command line 
            process = subprocess.Popen("java -jar " + sys.argv[1])    
            time.sleep(2)
            if(process.returncode != None):
                Debug.BMLog("Couldnt locate jar file or java isnt installed")
                return       


        
    Debug.BMLog("Continuing program")
    
    



        

            

    
  


if __name__ == "__main__":
    main()