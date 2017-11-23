import botModule as Bot
import pointLibrary as PointLib

import guildModule as Guild

# Fortress methods
def farmFortressXp(hoursToFarm):
    print ('Going to farm fortress xp for ' + str(hoursToFarm) + ' hours.')
    Bot.printTime()

    timeNow = Bot.getTime()
    for i in range(hoursToFarm):
        timeNow = Bot.getTime()
        
        if (timeNow.hour > 23 or timeNow.hour < 4):
            browserProcess = Bot.openBrowser()
            collectGuardDutyReward()
            collectFortressRessources()
            Guild.enlistToGuildFights()
            browserProcess.kill()
            print ('It is time to sleep now.')
            return 

        browserProcess = Bot.openBrowser()
        collectGuardDutyReward()
        startGuardDutyHours(1)
        collectFortressRessources()
        browserProcess.kill()
        Bot.sleep(60 * 59)


def startGuardDutyHours(hours):
    print('Working as guard for ' + str(hours) + ' hours.')
    Bot.click(PointLib.guardDutyMenuButton)
    Bot.click(PointLib.guardDutyOkButton)

def collectGuardDutyReward():
    Bot.click(PointLib.guardDutyMenuButton)

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


