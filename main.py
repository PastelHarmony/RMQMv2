from player import Player
from room import Room
from item import Item
from util import Util
from npc import NPC
from npc import Creature
from npc import Character
from event import Quest
from event import Story
from event import Random

# TODO
# talk
# give
# quest
# quests
# events
# random events
# dates, seasons, holidays
# npcs
# fans (items)
# food
# drink
# health, medicine
# farming
# animals
# cooking
# crafting
# put and take multiples of items
# make talismans??
# saving

player = Player()

qk_pouch = Item("Qiankun pouch",
                f'A small {player.sectcolors} bag made of thick silk. It is secured with a silver drawstring and embroidered with intricate {player.sectsym}s. It can hold an unlimited amount of objects.',
                "container", True, True, False, True, {}, False, "in", {})

# rooms: loc, subloc, daydesc, nightdesc, raindesc, snowdesc, gendesc, items, hiddenitems, npcs

start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.",
                  "Silver moonlight gently brushes along the walls.",
                  "The pattering of the rain echoes loudly through the dim room.",
                  "Snow twirls outside the window, blowing wildly in the wind.",
                  "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.",
                  {qk_pouch.itemname: qk_pouch}, {}, {}, {})
qk_pouch.amount[start_room] = 1
player.playloc = start_room

# items: itemname, itemdesc, type, uses, canTake, canPush, isRegenerative, amnt, isContainer, contents, isLocked, inoron, isLiquid, isFood, restores, isIngredient, isCrafter, isTool

zhan_disc_robe = Item("Zhan disciple robe",
                      "Standard Zhan disciple robes made of a thick, crimson fabric weighted at the edges to give a foreboding silhouette. Between each layer is a thin sheet of plated metal etched with flames.",
                      "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
sheng_disc_robe = Item("Sheng disciple robe",
                       "Standard Sheng disciple robes made of a shimmering, intricately embroidered golden cloth. They are covered in the unmistakable swirling koi of the Sheng sect.",
                       "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
yong_disc_robe = Item("Yong disciple robe",
                      "Standard Yong disciple robes made of simple, firm cloth doused in deep viridian. They are comfortable and easy to move in, suited for long hours of training.",
                      "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
yi_disc_robe = Item("Yi disciple robe",
                    "Standard Yi disciple robes made of rich sapphire blue. They are high-necked and long-sleeved, with stiff under-layers and draping outer-layers that obscure the figure.",
                    "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
min_disc_robe = Item("Min disciple robe",
                     "Standard Min disciple robes made of a light, flowing fabric in rippling hues of lilac. With many stacked thin layers meant to imitate a rose, they create an ethereal figure.",
                     "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
wu_disc_robe = Item("Wu disciple robe",
                    "Standard Wu disciple robes in dark onyx, flexible and sleek. They are covered in a sturdy yet lightweight hooded cloak.",
                    "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False)
yong_dadao = Item("Yong dadao", f'A large, hefty dadao in a dark green sheath.', "sword", True, True, False, {}, False,
                  None, None, None, False, False, None, False, False, False)
zhan_zhanmadao = Item("Zhan zhanmadao", f'A powerful two-handed zhanmadao in a crimson sheath.', "sword", True, True,
                      False, {}, False, None, None, None, False, False, None, False, False, False)
sheng_hudiedao = Item("Sheng hudiedao", f'A thin, wide hudiedao in a golden sheath.', "sword", True, True, False, {}, False,
                      None, None, None, False, False, None, False, False, False)
yi_taijijian = Item("Yi taijijian", f'A sharp, lightweight spiritual taijijian in a sapphire sheath.', "sword", True,
                    True, False, {}, False, None, None, None, False, False, None, False, False, False)
wu_hooksword = Item("Wu hook swords", f'Two deadly, versatile hook swords in onyx sheaths.', "sword", True, True, False,
                    {}, False, None, None, None, False, False, None, False, False, False)
min_wodao = Item("Min wodao", f'A long, slender wodao in a lilac sheath.', "sword", True, True, False, {}, False, None,
                 None, None, False, False, None, False, False, False)


# npcs:

# quests:

# random events:

# story events:

def setinfo(player):
    player.surname = input("What is your surname? : ").capitalize()
    player.birthname = input("What is your birthname? : ").capitalize()
    player.courtname1 = input("What is the first syllable of your courtesy name? : ").capitalize()
    player.courtname2 = input("What is the second syllable of your courtesy name? : ").capitalize()
    player.courtname = player.courtname1 + player.courtname2.lower()
    player.setprn(
     input(
      "What are your pronouns? (Please express as \"she/her\", \"he/him\", \"they/them\", \"it/its\", or \"other\") "))
    player.sethonorific(input(
     "Would you rather be called: 1. Meimei (younger sister) and jiejie (older sister), or 2. Didi (younger brother) and gege (older brother)? (The option to choose neither will be coming in later updates.) "))
    swordname = input("What is your sword's name? ")
    playersect = input("""What sect are you from?
    Yandi Zhan - The Zhan sect is an extensive militaristic sect located in the forests below the Huangling Sheng. It is also bordered by the Antian Yi and Liangzi Min to the west and by the Jingnong Yong and Qiaoxue Wu to the east. Below it lies the ocean.
    Huangling Sheng - The Sheng sect is a fairly large sect with a prosperous trading economy. It is located near a snowy mountain range that feeds into many large rivers and bordered below by the Yandi Zhang, the Antian Yi, and the Jingnong Yong. Its east side reaches the sea.
    Antian Yi - The Yi sect is a moderately small but widely influential sect that focuses on self-enlightenment and justice. It is bordered on the north by the Huangling Sheng, on the south by the Liangzi Min, and to the east by the Yandi Zhang. It is also known for its beautiful waterfalls.
    Jingnong Yong - The Yong sect is a wide agricultural sect in the plains below the Huangling Sheng and to the east of the Yandi Zhan. Its people are known to be diligent and hard-working. Below it lies the Qiaoxue Wu.
    Liangzi Min - The Min sect is a scholarly sect of intermediate size with rolling hills and sparkling lakes fed by the many bays below it. It is bordered by the Antian Yi on the north and the Yandi Zhang on the east.
    Qiaoxue Wu - The Wu sect is on the smaller side, but it is one of the oldest that still exists. It has magnificent cave systems and shadowy forests. It is also heavily shrouded in mystery; Despite this, it is known for producing great works of art. It is located to the south of the Jingnong Yong and to the east of the Yandi Zhan.
    (Please reply with full sect name): """).title()
    player.setsect(playersect, swordname, zhan_zhanmadao, sheng_hudiedao, yi_taijijian, yong_dadao, min_wodao,
                   wu_hooksword,
                   zhan_disc_robe, sheng_disc_robe, yi_disc_robe, yong_disc_robe, min_disc_robe, wu_disc_robe)
    print(
     f'Your name is {player.surname} {player.birthname}, courtesy {player.courtname}. Your pronouns are {player.pronouns["subjprn"]}/{player.pronouns["objprn"]}/{player.pronouns["posadj"]}/{player.pronouns["posprn"]}/{player.pronouns["refprn"]}. Your elders may refer to you as {player.meiordi}{player.meiordi}. Your juniors may refer to you as {player.jieorge}{player.jieorge}. You are a twenty-one-year-old cultivator from the {player.sect} sect, and your sword is named {swordname}. You are in your room at Laolu inn in Baiping village on a mission to exorcise a vengeful ghost.')
    del swordname
    if input("Is this correct? (Yes/No): ") == "No":
     setinfo(player)

time = "day"

print("""
Welcome to Rolling Mists, Quiet Moons.
Rolling Mists, Quiet Moons is a text-based adventure developed in Python by Abigail Hui. It is set in fantastical ancient China. Previous knowledge of "xianxia" is strongly recommended but not required.
""")
ready = input("Please press enter when you are ready to begin the game. ")
if ready == "":
    print("Loading...")
print(start_room.getdescription(time))
print(
    "Your eyes flicker open slowly. You take a moment to gather yourself. As you blink away the haze of sleep, your memories come trickling back to you.")
setinfo(player)
Util.runact(player, qk_pouch, input(""), time)
