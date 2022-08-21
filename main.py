from player import Player
from room import Room
from item import Item
from util import Util

# TODO (functions)
# wear
# undress
# talk
# give
# quest

player = Player()

qk_pouch = Item("Qiankun pouch", f'A small {player.sectcolors} bag made of thick silk. It is secured with a silver drawstring and embroidered with intricate {player.sectsym}s. It can hold an unlimited amount of objects.', "container",
                {}, True, True, False, True, {}, False, "in", {})

start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.", "Silver moonlight gently brushes along the walls.", "The pattering of the rain echoes loudly through the dim room.", "Snow twirls outside the window, blowing wildly in the wind.", "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.", {qk_pouch.itemname:qk_pouch}, {}, {})
qk_pouch.amount[start_room] = 1
player.playloc = start_room
robe = Item("robe", "A white fish.", "robe", {}, True, True, False, False, None, None, None, {player:1})
player.onplayer[robe.itemname] = robe

time = "day"

print("""
Welcome to Rolling Mists, Quiet Moons.
Rolling Mists, Quiet Moons is a text-based adventure developed in Python by Abigail Hui. It is set in fantastical ancient China. Previous knowledge of "xianxia" is strongly recommended but not required.
""")
ready = input("Please press enter when you are ready to begin the game. ")
if ready == "":
 print("Loading...")
print(start_room.getdescription(time))
print("Your eyes flicker open slowly. You take a moment to gather yourself. As you blink away the haze of sleep, your memories come trickling back to you.")
player.surname = input("What is your surname? (Please capitalize first letter): ")
player.birthname = input("What is your birthname? (Please capitalize first letter): ")
player.courtname1 = input("What is the first syllable of your courtesy name? (Please capitalize first letter): ")
player.courtname2 = input("What is the second syllable of your courtesy name? (Please capitalize first letter): ")
player.setcourtname()
player.setprn(input("What are your pronouns? (Please express as \"she/her\", \"he/him\", \"they/them\", \"it/its\", or \"other\") "), input("Would you rather be called: 1. Meimei (younger sister) and jiejie (older sister), or 2. Didi (younger brother) and gege (older brother)? (The option to choose neither will be coming in later updates.) "))
swordname = input("What is your sword's name? ")
playersect = input("""What sect are you from?
Yandi Zhan - The Zhan sect is an extensive militaristic sect located in the forests below the Huangling Sheng. It is also bordered by the Antian Yi and Liangzi Min to the west and by the Jingnong Yong and Qiaoxue Wu to the east. Below it lies the ocean.
Huangling Sheng - The Sheng sect is a fairly large sect with a prosperous trading economy. It is located near a snowy mountain range that feeds into many large rivers and bordered below by the Yandi Zhang, the Antian Yi, and the Jingnong Yong. Its east side reaches the sea.
Antian Yi - The Yi sect is a moderately small but widely influential sect that focuses on self-enlightenment and justice. It is bordered on the north by the Huangling Sheng, on the south by the Liangzi Min, and to the east by the Yandi Zhang. It is also known for its beautiful waterfalls.
Jingnong Yong - The Yong sect is a wide agricultural sect in the plains below the Huangling Sheng and to the east of the Yandi Zhan. Its people are known to be diligent and hard-working. Below it lies the Qiaoxue Wu.
Liangzi Min - The Min sect is a scholarly sect of intermediate size with rolling hills and sparkling lakes fed by the many bays below it. It is bordered by the Antian Yi on the north and the Yandi Zhang on the east.
Qiaoxue Wu - The Wu sect is on the smaller side, but it is one of the oldest that still exists. It has magnificent cave systems and shadowy forests. It is also heavily shrouded in mystery; Despite this, it is known for producing great works of art. It is located to the south of the Jingnong Yong and to the east of the Yandi Zhan.
(Please reply with full sect name. Capitalization is important): """)
player.setsect(playersect)
print(f'Your name is {player.surname} {player.birthname}, courtesy {player.courtname}. Your pronouns are {player.pronouns["subjprn"]}/{player.pronouns["objprn"]}/{player.pronouns["posadj"]}/{player.pronouns["posprn"]}/{player.pronouns["refprn"]}. Your elders may refer to you as {player.meiordi}{player.meiordi}. Your juniors may refer to you as {player.jieorge}{player.jieorge}. You are a twenty-one-year-old cultivator from the {player.sect} sect, and your sword is named {swordname}. You are in your room at Laolu inn in Baiping village on a mission to exorcise a vengeful ghost.')
Util.runact(player, qk_pouch, input(""), time)