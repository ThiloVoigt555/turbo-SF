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


def doGuardDutyForHours():
    print('Working as guard.')
    Bot.click(PointLib.guardDutyMenuButton)
    # TODO implement
    
# Debugging:

#Bot.getCheckpointAtCurser()
#enlistToGuildFights()
#collectFortressRessources()
#quest.test()
#sys.exit()



# Main
print('Starting up the bot:')

for i in range(6):
    Bot.sleep(1)

#Arena.completeArena(10)
#Bot.waitUntilTomorrow(5)

while(True):
    Quest.completeQuests()

    print ('Cooling down for a while.')
    Bot.sleep(60 * 5)

    Arena.completeArena(34)

    #Fortress.farmFortressXp(9)
    
    Bot.waitUntilTomorrow(5)
    
