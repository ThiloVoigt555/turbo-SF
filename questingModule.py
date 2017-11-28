import botModule as Bot
import pointLibrary as PointLib
import globalConstants as Constants

import fortressModule as Fortress
import guildModule as Guild


# Questing methods 
def completeQuests():
    print ('Started questing.')
    browserProcess = Bot.openBrowser()
    Fortress.collectFortressRessources()
    Guild.enlistToGuildFights()
    
    for i in range(30):
        moreToGo = runQuest(i)
        if moreToGo == False:
            Bot.printTime()
            print ('All Quests finished')
            browserProcess.kill()
            return False

        if (i % 3 == 0 and i != 0):
            browserProcess.kill()
            Bot.sleep(60 * (14 - Constants.firefoxStartupTime))
            browserProcess = Bot.openBrowser()
            Fortress.collectFortressRessources()

        else:
            Bot.sleep(60 * 14)
        
    print ('More than 30 quests needed!')
    browserProcess.kill()

def runQuest(index):
    print ('Quest #' + str(index))
    Bot.click(PointLib.tavernMenuButton)
    Bot.sleep(10)
    Bot.click(PointLib.tavernMenuButton)
    
    if allQuestsDone():
        return False
    
    Bot.click(PointLib.questGuy)
    chosenQuest = chooseQuest(str(index))
    if chosenQuest == 1:
        Bot.click(PointLib.firstQuest)
    elif chosenQuest == 2:
        Bot.click(PointLib.secondQuest)
    elif chosenQuest == 3:
        Bot.click(PointLib.thirdQuest)
        
    Bot.click(PointLib.questOkButton)
    Bot.sleep(25)
    Bot.click(PointLib.characterMenuButton)

def allQuestsDone():
    if isAluEmpty():
        if isMushroomEvent():
           drinkBeers()
           if isAluEmpty():
               return True
        else:
            return True
    else:
        return False

def isAluEmpty():
    return Bot.checkPixel(PointLib.aluCheckPoint)

def isMushroomEvent():
    return Bot.checkPixel(PointLib.mushroomEventCheckPoint)

def drinkBeers():
    Bot.click(PointLib.beerGuy)
    for i in range(5):
        Bot.click(PointLib.drinkBeerButton)
        
    Bot.click(PointLib.drinkBeerBackButton)

def chooseQuest(questNumber):
    if (int(questNumber) < 10):
        questNumber = '0' + questNumber
        
    #print ('Choosing quest for quest #' + index)
    firstQuota = extractXpQuota(PointLib.firstQuest, questNumber, '1')
    secondQuota = extractXpQuota(PointLib.secondQuest, questNumber, '2')
    thirdQuota = extractXpQuota(PointLib.thirdQuest, questNumber, '3')
    
    results = [firstQuota, secondQuota, thirdQuota]
    chosenQuestIndex = max(enumerate(results), key=lambda x: x[1])[0]
    #print ('Chosen quest: ' + str(chosenQuest + 1))
    return chosenQuestIndex + 1

def extractXpQuota(questProposalPoint, questNumber, questProposalIndex):
    Bot.click(questProposalPoint)
    questData = getQuestInfo(questNumber + questProposalIndex)
    quota = getXpQuota(questData)
    #print (questData[0] + ', ' + questData[1] + ' quota: ' + str(quota))
    return quota

def getQuestInfo(index):
    filename = index + 'xpValue' + '.png'
    rawXpValue = readScreenArea(filename, PointLib.questXpArea, ',')
    xpValue = interpretXpValue(rawXpValue)

    filename = index + 'durationValue' + '.png'
    rawDurationValue = readScreenArea(filename, PointLib.questDurationArea, ':')
    durationValue = interpretDurationValue(rawDurationValue)

    return (xpValue, durationValue)

def readScreenArea(fileName, screenArea, separationCaracter):
    Bot.saveScreenshot(fileName, screenArea)
    rawXpValue = Bot.runOCR(fileName, separationCaracter)
    return rawXpValue

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

def getXpQuota(questData):
    try:
        return int(questData[0]) / int(questData[1])
    except:
        return 0.0
