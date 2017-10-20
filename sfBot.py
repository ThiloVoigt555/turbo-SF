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
gameScreenCheckPoint = ((1323, 874), (247, 133, 129)) #((1493, 854), (16, 38, 52))
gameScreenPopupReset = (1324, 742)
logInButton = (855, 842)

tavernMenuButton = (65, 241)
tavernCheckPoint = ((346, 857), (72, 58, 47))
characterMenuButton = (78, 694)
areaMenuButton = (73, 293)
fortressMenuButton = (50, 939)

questGuy = (633, 687)
firstQuest = (430, 721)
secondQuest = (424, 764)
thirdQuest = (425, 808)
questXpArea = (756, 751, 100, 24) 
questDurationArea = (738, 795, 80, 24)
questOkButton = (1048, 734)
aluCheckPoint = ((484, 898), (0, 26, 39))

firstArenaEnemy = (603, 397)
arenaOkButton = (904, 710)

fortressPopupReset = (265, 554)
fortressXpBuilding = (403, 442)
fortressStoneBuilding = (398, 757)
fortressWoodBuilding = (542, 827)


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
        click(gameScreenPopupReset)
        if (checkPixel(gameScreenCheckPoint)):
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

def interpretXpValue(valueString):
    valueString = valueString.replace(' ', '')
    valueString = valueString.replace(',', '')
    return valueString

def interpretDurationValue(valueString):
    valueString = valueString.replace(' ', '')
    valueString = valueString.replace(':', '')
    if (valueString != '' and int(valueString) > 9999):
        valueString = '1400'
    return valueString

def saveScreenshot(fileName, area):
    x,y,w,h = [str(x) for x in area]
    subprocess.call(['maim', '-x', x, '-y', y, '-w', w, '-h', h, fileName])

def getQuestInfo(index):
    filename = index + 'xpValue' + '.png'
    saveScreenshot(filename, questXpArea)
    rawXpValue = runOCR(filename, ',')
    xpValue = interpretXpValue(rawXpValue)

    filename = index + 'durationValue' + '.png'
    saveScreenshot(filename, questDurationArea)
    rawDurationValue = runOCR(filename, ':')
    durationValue = interpretDurationValue(rawDurationValue)

    return (xpValue, durationValue)



# Questing methods    
def runQuest(index):
    print ('Starting a quest.')
    click(tavernMenuButton)
    time.sleep(10)
    click(tavernMenuButton)
    if aluIsEmpty():
        return False
    click(questGuy)

    chosenQuest = chooseQuest(str(index))
    if chosenQuest == 1:
        click(firstQuest)
    elif chosenQuest == 2:
        click(secondQuest)
    elif chosenQuest == 3:
        click(thirdQuest)
        
    click(questOkButton)
    time.sleep(25)
    click(characterMenuButton)

def aluIsEmpty():
    return checkPixel(aluCheckPoint)

def completeQuests():
    print ('Started questing.')
    browserProcess = openBrowser()
    collectFortressRessources()
    
    for i in range(20):
        questResult = runQuest(i) 
        if questResult == False:
            print ('All Quests finished')
            browserProcess.kill()
            return False

        if (i % 3 == 0 and i != 0):
            browserProcess.kill()
            time.sleep(60 * (14 - _firefoxStartupTime))
            browserProcess = openBrowser()
            collectFortressXp()

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
        
def completeArena(trys):
    print ('Arena fighting:')
    browserProcess = openBrowser()
    collectFortressRessources()
    
    for i in range(trys):
        runArenaFight()

        if (i % 2 == 0 and i != 0):
            browserProcess.kill()
            time.sleep(60 * (10 - _firefoxStartupTime))
            browserProcess = openBrowser()
            collectFortressXp()
            
        else:
            time.sleep(60 * 10)
        print ('Done with arena-sleep.')

    browserProcess.kill()
    print ('Done with all fights.')



# Fortress methods
def collectFortressRessources():
    print ('Collecting all fortress ressources.')
    click(fortressMenuButton)
    time.sleep(10)
    click(fortressXpBuilding)
    click(fortressPopupReset)
    click(fortressStoneBuilding)
    click(fortressPopupReset)
    click(fortressWoodBuilding)
    click(fortressPopupReset)
    click(characterMenuButton)

def collectFortressXp():
    print ('Collecting fortress xp.')
    click(fortressMenuButton)
    time.sleep(10)
    click(fortressXpBuilding)
    click(characterMenuButton)




# Beta Methods
def getXpQuota(questData):
    try:
        # TODO sanity checks
        return int(questData[0]) / int(questData[1])
    except:
        return 0.0
    
def chooseQuest(index):
    if (int(index) < 10):
        index = '0' + index
        
    print ('Choosing quest for quest #' + index)
    
    click(firstQuest)
    firstQuestData = getQuestInfo(index + '1')
    firstQuota = getXpQuota(firstQuestData)
    print (firstQuestData[0] + ', ' + firstQuestData[1] + ' quota: ' + str(firstQuota))
    
    click(secondQuest)
    secondQuestData = getQuestInfo(index + '2')
    secondQuota = getXpQuota(secondQuestData)
    print (secondQuestData[0] + ', ' + secondQuestData[1] + ' quota: ' + str(secondQuota))
           
    click(thirdQuest)
    thirdQuestData = getQuestInfo(index + '3')
    thirdQuota = getXpQuota(thirdQuestData)
    print (thirdQuestData[0] + ', ' + thirdQuestData[1] + ' quota: ' + str(thirdQuota))

    results = [firstQuota, secondQuota, thirdQuota]
    chosenQuest = max(enumerate(results), key=lambda x: x[1])[0]
    print ('Chosen quest: ' + str(chosenQuest + 1))

    return chosenQuest + 1


def enlistToGuildFights():
    return

def doDailys():
    # TODO spin round
    return

def farmFortressXp(hoursToFarm):
    timeNow = datetime.datetime.now()
    print ('Time: ' + str(timeNow.hour) + ':' + str(timeNow.minute))
    print ('Going to farm fortress xp for ' + str(hoursToFarm) + ' hours.')
    
    for i in range(hoursToFarm):
        timeNow = datetime.datetime.now()
        if (timeNow.hour > 21 or timeNow.hour < 4):
            print ('Time to sleep now. No more Fortress farming!')
            return 

        
        browserProcess = openBrowser()
        collectFortressXp()
        browserProcess.kill()
        time.sleep(60 * 53)


getCheckpointAtCurser()

#openBrowser()

#collectFortressRessources()
#print (result)
sys.exit()
# http://w19.sfgame.net/?playerclass=1&platform=html5



# Main
print('Starting up the bot:')
for i in range(6):
    time.sleep(1)

while(True):    
    completeQuests()

    print ('Cooling down for a while.')
    time.sleep(60 * 6)
    
    completeArena(15)

    farmFortressXp(6)
    
    waitUntilTomorrow(5)
    

