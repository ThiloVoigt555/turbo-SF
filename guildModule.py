import botModule as Bot
import pointLibrary as PointLib
import globalConstants as Constants


# Guild methods
def enlistToGuildFights():
    print('Enlisting to guild fights.')
    Bot.click(PointLib.guildMenuButton)
    Bot.sleep(10) 
    Bot.click(PointLib.guildAttackEnlist)
    Bot.click(PointLib.guildDefenseEnlist)
    Bot.click(PointLib.guildRaidEnlist)

def spinWheelOfFortune():
    print('Spinning the wheel of fortune.')
    Bot.click(PointLib.abawuwuMenuButton)
    Bot.click(PointLib.abawuwuSpinWheel)
