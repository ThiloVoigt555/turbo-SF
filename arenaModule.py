import pointLibrary as PointLib
import botModule as Bot
import globalConstants as Constants

import fortressModule as Fortress
import guildModule as Guild


# Arena methods
def completeArena(trys):
    print ('Arena fighting:')
    browserProcess = Bot.openBrowser()
    Fortress.collectFortressRessources()
    Guild.enlistToGuildFights()
    
    for i in range(trys):
        if (timeNow.hour > 23 or timeNow.hour < 4):
            print ('It is time to sleep now.')
            return
        
        runArenaFight(i)

        if (i % 2 == 0 and i != 0):
            browserProcess.kill()
            Bot.sleep(60 * (10 - Constants.firefoxStartupTime))
            browserProcess = Bot.openBrowser()
            Fortress.collectFortressRessources()
            
        else:
            Bot.sleep(60 * 10)

    browserProcess.kill()
    Bot.printTime()
    print ('Done with all fights.')

    
def runArenaFight(index):
    print ('Area Fight #' + str(index))
    Bot.click(PointLib.areaMenuButton)
    Bot.sleep(30)
    Bot.click(PointLib.firstArenaEnemy)
    Bot.click(PointLib.arenaOkButton)
    Bot.time.sleep(60)
    Bot.click(PointLib.characterMenuButton)
