import time
import subprocess
import pytesseract
import pyautogui
import datetime
import sys
from PIL import Image

import pointLibrary as PointLib
import globalConstants as Constants


# pyAutoGui Settings
pyautogui.FAILSAFE = Constants.failSave
pyautogui.PAUSE = Constants.autoGuiPause


# Util methods
def sleep(seconds):
    time.sleep(seconds)

def getTime():
    return datetime.datetime.now()

def printTime():
    timeNow = getTime()
    print ('Time: ' + str(timeNow.hour) + ':' + str(timeNow.minute))
    
def click(point):
    pyautogui.click(point[0], point[1])

def checkPixel(checkPoint):
    return pyautogui.pixelMatchesColor(checkPoint[0][0], checkPoint[0][1], checkPoint[1], tolerance=10)

def getCheckpointAtCurser():
    posX, posY = pyautogui.position()
    print('(('+ str(posX) + ', ' + str(posY) + '), ' + str(pyautogui.pixel(posX, posY)) + ')')

def waitUntilTomorrowAt(hourToStop):
    print ('Day completed. Gonna sleep until tomorrow.')
    print ('')
    timeNow = datetime.datetime.now()
    while(timeNow.hour != hourToStop):
        timeNow = datetime.datetime.now()
        time.sleep(60 * 41)
    print ('A new day!')

def openBrowser():
    for i in range(5):
        print ('Opening Firefox.')
        browserProcess = subprocess.Popen(['firefox', 'http://w20.sfgame.net/?playerclass=1&platform=html5'])    
        time.sleep(60 * Constants.firefoxStartupTime)
        click(PointLib.gameScreenPopupReset)
        if (checkPixel(PointLib.gameScreenCheckPoint)):
            print ('Game is running.')
            return browserProcess
            
        pyautogui.screenshot('browserFail.png')
        browserProcess.kill()
        
    print ('Browser failed to load the game')
    sys.exit()

def logIn():
    click(logInButton)
    time.sleep(30)

def runOCR(filename, possibleChar):
    return pytesseract.image_to_string(Image.open(filename), config='-psm 8 -c tessedit_char_whitelist=0123456789' + possibleChar)

def saveScreenshot(fileName, area):
    x,y,w,h = [str(x) for x in area]
    subprocess.call(['maim', '-x', x, '-y', y, '-w', w, '-h', h, fileName])
