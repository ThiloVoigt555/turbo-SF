import sys
import datetime

import questingModule as Quest
import botModule as Bot
import arenaModule as Arena
import pointLibrary as PointLib
import globalConstants as Constants
import fortressModule as Fortress
import guildModule as Guild



# Beta Methods

    
# Debugging:

#Bot.getCheckpointAtCurser()
#enlistToGuildFights()
#collectFortressRessources()
#result = Quest.isMushroomEvent()
#print(result)
#sys.exit()



# Main
print('Starting up the bot:')

for i in range(6):
    Bot.sleep(1)

#Arena.completeArena(5)
#Fortress.farmFortressXp(9)
#Bot.waitUntilTomorrowAt(5)

while(True):
    Quest.completeQuests()

    Bot.sleep(60 * 2)

    Arena.completeArena(30)

    Fortress.farmFortressXp(10)
    
    Bot.waitUntilTomorrowAt(5)
    

