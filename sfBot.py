import sys
import datetime

import questingModule as Quest
import botModule as Bot
import arenaModule as Arena
import pointLibrary as PointLib
import globalConstants as Constants
import fortressModule as Fortress

# Beta Methods
def enlistToGuildFights():
    Bot.click(PointLib.guildMenuButton)
    Bot.click(PointLib.guildAttackEnlist)
    Bot.click(PointLib.guildDefenseEnlist)
    Bot.click(PointLib.guildRaidEnlist)

def spinWheelOfFortune():
    Bot.click(PointLib.abawuwuMenuButton)
    Bot.click(PointLib.abawuwuSpinWheel)

    
# Debugging:

#Bot.getCheckpointAtCurser()
#enlistToGuildFights()
#collectFortressRessources()
#quest.test()
#sys.exit()
# http://w19.sfgame.net/?playerclass=1&platform=html5



# Main
print('Starting up the bot:')

for i in range(6):
    Bot.sleep(1)

Arena.completeArena(3)
Bot.waitUntilTomorrow(5)

while(True):    
    Quest.completeQuests()

    print ('Cooling down for a while.')
    Bot.sleep(60 * 5)
    
    Arena.completeArena(30)

    #Fortress.farmFortressXp(9)
    
    Bot.waitUntilTomorrow(5)
    

