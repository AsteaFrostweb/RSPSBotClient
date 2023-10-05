import subprocess
import sys
import time
import ImageProcessing as IP
import Debug

maxWaitTime = 15.0
hasLauncher = False

def main():
    
    #checking if the command line argument for the botclient jar has been entered
    if(sys.argv[1] == ""):
        Debug.BMLog("Please edit run.bat to include the RSPS jar filename. Example: python BotManager.py [filename].jar")
        return
    

    print("Initializing RSPS Client")
    #Attempting to run the .jar through the command line with args[1] from the command line 
    process = subprocess.Popen("java -jar " + sys.argv[1])    
    if(process.returncode != None):
        Debug.BMLog("Couldnt locate jar file or java isnt installed")
        return        
   

    if(hasLauncher):
        #waiting till maxWaitTime for the windows to open
        startTime = time.time()
        elapsedTime = time.time() - startTime
        launched = False
        while(elapsedTime <= maxWaitTime):
            if(IP.DoesWindowExist("BlissScape 718")):
                Debug.BMLog("Launcher Opened")
                launched = True
                break
            else:
                Debug.BMLog("Waiting for laucher. Elapsed time: " + str(int(elapsedTime)))
            elapsedTime = time.time() - startTime
            time.sleep(1)

        if(launched == False):
            Debug.BMLog("Launcher didn't start in maximum alloted time. Ending program")
            return
        
    Debug.BMLog("Continuing program")
    
    



        

            

    
  


if __name__ == "__main__":
    main()