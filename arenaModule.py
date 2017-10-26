import pointLibrary as PointLib
import botModule as Bot
import globalConstants as Constants
import fortressModule as Fortress


# Arena methods
def completeArena(trys):
    print ('Arena fighting:')
    browserProcess = Bot.openBrowser()
    collectFortressRessources()
    
    for i in range(trys):
        runArenaFight(i)

        if (i % 2 == 0 and i != 0):
            browserProcess.kill()
            Bot.sleep(60 * (10 - Constants.firefoxStartupTime))
            browserProcess = Bot.openBrowser()
            collectFortressRessources()
            
        else:
            Bot.sleep(60 * 10)
        print ('Done with arena-sleep.')

    browserProcess.kill()
    Bot.printTime()
    print ('Done with all fights.')

    
def runArenaFight(index):
    print ('Area Fight #' + str(index))
    Bot.click(PointLib.characterMenuButton)
    Bot.click(PointLib.areaMenuButton)
    Bot.sleep(30)
    Bot.click(PointLib.firstArenaEnemy)
    Bot.click(PointLib.arenaOkButton)
    Bot.time.sleep(50)
    Bot.click(PointLib.characterMenuButton)
