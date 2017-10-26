import botModule as Bot
import pointLibrary as PointLib


# Fortress methods
def farmFortressXp(hoursToFarm):
    Bot.printTime()
    print ('Going to farm fortress xp for ' + str(hoursToFarm) + ' hours.')

    timeNow = Bot.getTimeNow()
    for i in range(hoursToFarm):
        timeNow = Bot.getTimeNow()
        if (timeNow.hour > 23 or timeNow.hour < 4):
            print ('Time to sleep now. No more Fortress farming!')
            return 

        browserProcess = Bot.openBrowser()
        Fortress.collectFortressRessources()
        browserProcess.kill()
        Bot.sleep(60 * 53)

def collectFortressRessources():
    print ('Collecting all fortress ressources.')
    Bot.click(PointLib.fortressMenuButton)
    Bot.sleep(10)
    Bot.click(PointLib.fortressXpBuilding)
    Bot.click(PointLib.fortressPopupReset)
    Bot.click(PointLib.fortressStoneBuilding)
    Bot.click(PointLib.fortressPopupReset)
    Bot.click(PointLib.fortressWoodBuilding)
    Bot.click(PointLib.fortressPopupReset)
    Bot.click(PointLib.characterMenuButton)

def collectFortressXp():
    print ('Collecting fortress xp.')
    Bot.click(PointLib.fortressMenuButton)
    Bot.sleep(10)
    Bot.click(PointLib.fortressXpBuilding)
    Bot.click(PointLib.characterMenuButton)


