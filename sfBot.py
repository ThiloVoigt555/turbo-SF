import sys
import datetime

import questingModule as Quest
import botModule as Bot
import arenaModule as Arena
import pointLibrary as PointLib
import globalConstants as Constants
import fortressModule as Fortress


# Debugging:


#getCheckpointAtCurser()

#openBrowser()

#collectFortressRessources()
#quest.test()
#sys.exit()
# http://w19.sfgame.net/?playerclass=1&platform=html5



# Main
print('Starting up the bot:')
for i in range(6):
    Bot.sleep(1)

while(True):    
    Quest.completeQuests()

    print ('Cooling down for a while.')
    Bot.sleep(60 * 6)
    
    Arena.completeArena(15)

    Fortress.farmFortressXp(9)
    
    Bot.waitUntilTomorrow(5)
    


# Beta Methods
def enlistToGuildFights():
    return

def doDailys():
    # TODO spin round
    return





