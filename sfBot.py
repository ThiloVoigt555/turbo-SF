import pyautogui
import time
import datetime
import sys
import subprocess
import pytesseract
from PIL import Image

# Some Settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 22

# Constants
_firefoxStartupTime = 4

# Points on screen
gameScreenCheckPoint = ((1493, 854), (16, 38, 52))
logInButton = (855, 842)

tavernMenuButton = (65, 241)
tavernCheckPoint = ((346, 857), (72, 58, 47))
characterMenuButton = (78, 694)
areaMenuButton = (73, 293)

questGuy = (633, 687)
firstQuest = (430, 721)
questXpArea = (757, 754, 100, 20)
questDurationArea = (738, 798, 80, 20)
questOkButton = (1048, 734)
aluCheckPoint = ((484, 898), (0, 26, 39))

firstArenaEnemy = (603, 397)
arenaOkButton = (904, 710)


# Util methods
def click(point):
    pyautogui.click(point[0], point[1])

def checkPixel(checkPoint):
    return pyautogui.pixelMatchesColor(checkPoint[0][0], checkPoint[0][1], checkPoint[1], tolerance=10)

def getCheckpointAtCurser():
    posX, posY = pyautogui.position()
    print('(('+ str(posX) + ', ' + str(posY) + '), ' + str(pyautogui.pixel(posX, posY)) + ')')

def waitUntilTomorrow(hourToStop):
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
        time.sleep(5)
        browserProcess = subprocess.Popen(['firefox', 'http://w19.sfgame.net/?playerclass=1&platform=html5'])    
        time.sleep(60 * _firefoxStartupTime)
        if checkPixel(gameScreenCheckPoint):
            print ('Game is running.')
            return browserProcess
        pyautogui.screenshot('browserFail.png')
        browserProcess.kill()
        
    print ('Browser failed to load the game')
    sys.exit()

def logIn():
    click(logInButton)
    time.sleep(30)

def runOCR(filename):
    return pytesseract.image_to_string(Image.open(filename), config='-psm 8')

def interpretXpValue(valueString):
    return valueString.replace(',', '')

def interpretDurationValue(valueString):
    return valueString.replace(':', '')

def saveScreenshot(fileName, area):
    x,y,w,h = [str(x) for x in area]
    subprocess.call(['maim', '-x', x, '-y', y, '-w', w, '-h', h, fileName])




# Questing methods    
def runQuest():
    print ('Starting a quest.')
    click(tavernMenuButton)
    click(tavernMenuButton)
    if aluIsEmpty():
        return False
    click(questGuy)
    click(firstQuest)
    click(questOkButton)
    time.sleep(20)
    click(characterMenuButton)

def aluIsEmpty():
    return checkPixel(aluCheckPoint)

def completeQuests():
    print ('Started questing.')
    browserProcess = openBrowser()
    for i in range(20):

        questResult = runQuest() 
        if questResult == False:
            print ('All Quests finished')
            browserProcess.kill()
            return False

        if (i % 3 == 0 and i != 0):
            browserProcess.kill()
            time.sleep(60 * (14 - _firefoxStartupTime))
            browserProcess = openBrowser()

        else:
            time.sleep(60 * 14)
        print ('Done with quest-sleep')
        
    print ('More than 20 quests needed!')
    browserProcess.kill()
        

# Arena methods
def runArenaFight():
    print ('Doning an arena fight')
    click(characterMenuButton)
    click(areaMenuButton)
    time.sleep(30)
    click(firstArenaEnemy)
    click(arenaOkButton)
    time.sleep(50)
    click(characterMenuButton)
        
def completeArena():
    print ('Arena fighting:')
    browserProcess = openBrowser()
    for i in range(15):

        runArenaFight()

        if (i % 2 == 0 and i != 0):
            browserProcess.kill()
            time.sleep(60 * (10 - _firefoxStartupTime))
            browserProcess = openBrowser()
            
        else:
            time.sleep(60 * 10)
        print ('Done with arena-sleep.')

    browserProcess.kill()
    print ('Done with all fights.')



# Beta Methods

def getQuestInfo():
    saveScreenshot('xpValue.png', questXpArea)
    rawXpValue = runOCR('xpValue.png')
    xpValue = interpretXpValue(rawXpValue)

    saveScreenshot('durationValue.png', questDurationArea)
    rawDurationValue = runOCR('durationValue.png')
    durationValue = interpretDurationValue(rawDurationValue)

    return (xpValue, durationValue)

def chooseQuest():
    # TODO click on first quest
    firstQuest = getQuestInfo()
    
    

#getCheckpointAtCurser()

#saveScreenshot('test2.png', questDurationArea)
#result = runOCR('test2.png')
result = getQuestInfo()
print (result)
#time.sleep(60 * 2)

sys.exit()
# http://w19.sfgame.net/?playerclass=1&platform=html5



# Main
print('Starting up the bot:')
time.sleep(2)
time.sleep(2)
time.sleep(2)
time.sleep(2)

while(True):
    
    completeQuests()

    print ('Cooling down for a while.')
    time.sleep(60 * 11)
    
    completeArena()
    
    waitUntilTomorrow(5)
    

