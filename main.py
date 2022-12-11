from player import Player
from room import Room
from item import Item
from util import Util
from npc import NPC
from npc import Creature
from npc import Character
from event import Event
from event import Quest
from event import Story
from event import Random

# TODO (in no particular order):
# talk (dialogue trees)
# give (^ also npcs)
# quests (wip)
# events (wip)
# random events (wip)
# dates, seasons, holidays, weather
# regeneration and time-based regeneration (time = days = how many times slept)
# npcs (wip)
# fans (items)
# food (wip)
# drink (wip)
# disease & medicine (wip)
# animals (random events, time based regen. drop meat 0^0)
# cooking (wip)
# crafting (wip)
# make talismans?? (hard)
# saving (how.)
# shopping
# consider reputation system?
# cheats

player = Player()

qk_pouch = Item("Qiankun pouch", "Qiankun pouches",
                f'A small {player.sectcolors} bag made of thick silk. It is secured with a silver drawstring and embroidered with intricate {player.sectsym}s. It can hold an unlimited amount of objects.',
                "container", True, True, False, {}, True, {}, False, "in", False, False, None, False, False, False, False, False, False, False, False, False)

# rooms: loc, subloc, daydesc, nightdesc, raindesc, snowdesc, gendesc, items, hiddenitems, npcs, hiddennpcs, connects

start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.",
                  "Silver moonlight gently brushes along the walls.",
                  "The pattering of the rain echoes loudly through the dim room.",
                  "Snow twirls outside the window, blowing wildly in the wind.",
                  "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.",
                  {qk_pouch.itemname:qk_pouch}, {}, {}, {}, {})
qk_pouch.amount[start_room] = 1
player.playloc = start_room
ll_hall_north = Room("Laolu Inn", "North Hall", "Sunshine bathes the hall in bright rays.", "The hall is dark except for twinkling speckles of starlight.", "", "", "The walls are worn with old stains and scuffs. To the west and east are two rooms, while your own room is to the north. There is a rickety spiral staircase leading down. On the other side of the staircase, to your south, is the south hall.", {}, {}, {}, {}, {"north":(start_room, "active")})
ll_hall_south = Room("Laolu Inn", "South Hall", "Sunshine bathes the hall in bright rays.", "The hall is dark except for twinkling speckles of starlight.", "", "", "The walls are worn with old stains and scuffs. To the west, east, and south are three rooms. There is a rickety spiral staircase leading down. On the other side of the staircase, to your north, is the north hall.", {}, {}, {}, {}, {})
ll_room_northwest = Room("Laolu Inn", "Northwest Room", "", "", "", "", "", {}, {}, {}, {}, {})
ll_room_northeast = Room("Laolu Inn", "Northeast Room", "", "", "", "", "", {}, {}, {}, {}, {})
ll_room_southwest = Room("Laolu Inn", "Southwest Room", "", "", "", "", "", {}, {}, {}, {}, {})
ll_room_southeast = Room("Laolu Inn", "Southeast Room", "", "", "", "", "", {}, {}, {}, {}, {})
ll_room_south = Room("Laolu Inn", "South Room", "", "", "", "", "", {}, {}, {}, {}, {})
ll_lobby = Room("Laolu Inn", "Lobby", "", "", "", "", "", {}, {}, {}, {}, {})
ll_gardens = Room("Laolu Inn", "Gardens", "Birds chirp on sprightly boughs that hang low over your head. Dappled sunlight shines through the bushy leaves.", "The sound of crickets fill the air, accompanied by the occasional owl's bold hoot.", "Rain pours down, pooling up in the soil. The scent of petrichor hangs rich in the air.", "Snow has piled up, fresh flakes bouncing off the tree branches and landing on the ground.", "The garden is a small plot of land with colorful flowers between cobbled paths.", {}, {}, {}, {}, {})
start_room.connects["south"] = (ll_hall_north, "active")
start_room.connects["north"] = (ll_gardens, "inactive")
ll_gardens.connects["south"] = (start_room, "inactive")
ll_hall_north.connects["south"] = (ll_hall_south, "active")
ll_hall_north.connects["west"] = (ll_room_northwest, "active")
ll_hall_north.connects["east"] = (ll_room_northeast, "active")
ll_room_northwest.connects["east"] = (ll_hall_north, "active")
ll_room_northeast.connects["west"] = (ll_hall_north, "active")
ll_hall_south.connects["north"] = (ll_hall_north, "active")
ll_hall_south.connects["west"] = (ll_room_southwest, "active")
ll_hall_south.connects["east"] = (ll_room_southeast, "active")
ll_hall_south.connects["south"] = (ll_room_south, "active")
ll_room_southwest.connects["east"] = (ll_hall_south, "active")
ll_room_southeast.connects["west"] = (ll_hall_south, "active")
ll_room_south.connects["north"] = (ll_hall_south, "active")

# items: itemname, pluralitemname, itemdesc, type, canTake, canPush, isRegenerative, amnt, isContainer, contents, isLocked, inoron, isLiquid, isFood, restores, isIngredient, isCrafter, isTool, isWet, isFrozen, isFlammable, canPlant, growtime, harvestamnt
ll_yr_window = Item("window", "windows", "A small circular window covered in translucent rice paper. It looks a little loose.", "furniture", False, True, False, {start_room:1}, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
start_room.hidden_items["window"] = ll_yr_window
zhan_disc_robe = Item("Zhan disciple robe", "Zhan disciple robes",
                      "Standard Zhan disciple robes made of a thick, crimson fabric weighted at the edges to give a foreboding silhouette. Between each layer is a thin sheet of plated metal etched with flames.",
                      "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
sheng_disc_robe = Item("Sheng disciple robe", "Sheng disciple robes",
                       "Standard Sheng disciple robes made of a shimmering, intricately embroidered golden cloth. They are covered in the unmistakable swirling koi of the Sheng sect.",
                       "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
yong_disc_robe = Item("Yong disciple robe", "Yong disciple robes",
                      "Standard Yong disciple robes made of simple, firm cloth doused in deep viridian. They are comfortable and easy to move in, suited for long hours of training.",
                      "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
yi_disc_robe = Item("Yi disciple robe", "Yi disciple robes",
                    "Standard Yi disciple robes in rich sapphire blue. They are high-necked and long-sleeved, with stiff under-layers and draping outer-layers that obscure the figure.",
                    "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
min_disc_robe = Item("Min disciple robe", "Min disciple robes",
                     "Standard Min disciple robes made of a light, flowing fabric in rippling hues of lilac. With many stacked thin layers meant to imitate a rose, they create an ethereal figure.",
                     "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
wu_disc_robe = Item("Wu disciple robe", "Wu disciple robes",
                    "Standard Wu disciple robes in dark onyx, flexible and sleek. They are covered in a sturdy yet lightweight hooded cloak.",
                    "robe", True, True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
yong_dadao = Item("Yong dadao", None, f'A large, hefty dadao in a dark green sheath.', "sword", True, True, False, {}, False,
                  None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
zhan_zhanmadao = Item("Zhan zhanmadao", None, f'A powerful two-handed zhanmadao in a crimson sheath.', "sword", True, True,
                      False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
sheng_hudiedao = Item("Sheng hudiedao", None, f'A thin, wide hudiedao in a golden sheath.', "sword", True, True, False, {}, False,
                      None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
yi_taijijian = Item("Yi taijijian", None, f'A sharp, lightweight spiritual taijijian in a sapphire sheath.', "sword", True,
                    True, False, {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
wu_hooksword = Item("Wu hook swords", None, f'Two deadly, versatile hook swords in onyx sheaths.', "sword", True, True, False,
                    {}, False, None, None, None, False, False, None, False, False, False, False, False, False, False, False, False)
min_wodao = Item("Min wodao", None, f'A long, slender wodao in a lilac sheath.', "sword", True, True, False, {}, False, None,
                 None, None, False, False, None, False, False, False, False, False, False, False, False, False)


# creatures: name, desc, drops, killxp, isPassive, isHostile, stats, afflictions, isLiquid

# npcs: desc, surname, birthname, courtname, npctitle, npcsect, npcnamelist, yournamelist, intlvls, relationship
# dictionary copy-paste: -2:f'', -1:f'', 0:f'', 1:f'', 2:f'', 3:f'', 4:f'', 5:f'', 6:f'', 7:f'', 8:f'', 9:f'', 10:f''
zhanjiuke = Character("",
                      "Zhan", "Mei", "Jiuke", "Kushao-jun", "Yandi Zhan",
                      {-2:"Kushao-jun", -1:"Kushao-jun", 0:"Kushao-jun", 1:"Kushao-jun", 2:"Zhan-zhongzhu", 3:"Zhan-qianbei", 4:"Zhan-dage", 5:"Jiu-dage", 6:"Jiu-dage", 7:"Mei-gege", 8:"Mei-gege", 9:"A-Mei", 10:"A-Mei"},
                      {-2:f'{player.surname} {player.courtname}', -1:f'{player.surname} {player.courtname}', 0:f'{player.surname} {player.courtname}', 1:player.courtname, 2:player.courtname, 3:f'{player.surname}-xiao{player.meiordi}', 4:f'{player.surname}-xiao{player.meiordi}', 5:f'{player.courtname1}-xiao{player.meiordi}', 6:f'{player.courtname1}-xiao{player.meiordi}', 7:f'{player.courtname1}-xiao{player.meiordi}', 8:f'{player.birthname}-xiao{player.meiordi}', 9:f'{player.birthname}-xiao{player.meiordi}', 10:f'A-{player.birthname}'},
                      {-2:-50, -1:-25, 0:0, 1:50, 2:100, 3:150, 4:200, 5:300, 6:400, 7:500, 8:600, 9:750, 10:900},
                      {-2:"Enemy", -1:"Annoyance", 0:"Stranger", 1:"Acquaintance", 2:"Associate", 3:"Colleague", 4:"Companion", 5:"Friend", 6:"Ally", 7:"Confidant", 8:"Dear", 9:"Beloved", 10:"Soulmate"})
# zhanjiumai = Character("",
#                        "Zhan", "Xiu", "Jiumai", "", "Yandi Zhan",
#                        {},
#                        {},
#                        {},
#                        {})
yongwenshi = Character("",
                       "Yong", "Yan", "Wenshi", "Qinfen-jun", "Jingnong Yong",
                       {-2:"Qinfen-jun", -1:"Qinfen-jun", 0:"Qinfen-jun", 1:"Yong-zhongzhu", 2:"Yong-dajie", 3:"Wenshi-dajie", 4:"Wenshi-dajie", 5:"Wen-jiejie", 6:"Wen-jiejie", 7:"Yan-jie", 8:"Yan-jie", 9:"Yong Yan", 10:"A-Yan"},
                       {-2:f'{player.surname} {player.courtname}', -1:f'{player.surname} {player.courtname}', 0:f'{player.surname} {player.courtname}', 1:f'{player.courtname}', 2:f'{player.courtname}', 3:f'{player.courtname1}-{player.meiordi}', 4:f'{player.courtname1}-{player.meiordi}', 5:f'{player.surname} {player.birthname}', 6:f'{player.surname} {player.birthname}', 7:f'Xiao-{player.birthname}', 8:f'Xiao-{player.birthname}', 9:f'A-{player.birthname}', 10:f'A-{player.birthname}'},
                       {-2:-100, -1:-50, 0:0, 1:25, 2:50, 3:100, 4:150, 5:250, 6:350, 7:450, 8:550, 9:700, 10:800},
                       {-2:"Enemy", -1:"Adversary", 0:"Stranger", 1:"Acquaintance", 2:"Colleague", 3:"Friend", 4:"Comrade", 5:"Ally", 6:"Confidant", 7:"Best Friend", 8:"Kindred Spirit", 9:"Lover", 10:"Soulmate"})
#yong wenshi's brother
shengsulian = Character("",
                        "Sheng", "Biao", "Sulian", "Xingrong-jun", "Huangliang Sheng",
                        {-2:"Xingrong-jun", -1:"Xingrong-jun", 0:"Xingrong-jun", 1:"Xingrong-jun", 2:"Sheng-zhongzhu", 3:"Sheng-qianbei", 4:"Sheng-xiansheng", 5:"Sheng-xiansheng", 6:"Sulian-xiong", 7:"Sheng Sulian", 8:"Sulian", 9:"Sheng Biao", 10:"A-Biao"},
                        {-2:"", -1:"", 0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:""},
                        {-2:-150, -1:-100, 0:0, 1:50, 2:75, 3:200, 4:300, 5:450, 6:525, 7:625, 8:750, 9:900, 10:1000},
                        {-2:"Threat", -1:"Hazard", 0:"Pest", 1:"Nuisance", 2:"Pawn", 3:"Puppet", 4:"Tool", 5:"Acquaintance", 6:"Colleague", 7:"Friend", 8:"Ally", 9:"Confidant", 10:"Soulmate"})
# yizunxiao = Character("",
#                        "Yi", "Shi", "Zunxiao", "", "Antian Yi",
#                        {},
#                        {},
#                        {},
#                        {})
# yifanzai = Character("",
#                        "Yi", "Xian", "Fanzai", "", "Antian Yi",
#                        {},
#                        {},
#                        {},
#                        {})
# #hai yi?
# minguangjian = Character("",
#                        "Min", "Lan", "Guangjian", "", "Liangzi Min",
#                        {},
#                        {},
#                        {},
#                        {})
# wulueyuan = Character("",
#                        "Wu", "Yin", "Lueyuan", "", "Qiaoxue Wu",
#                        {},
#                        {},
#                        {},
#                        {})
# wuquanya = Character("",
#                        "Wu", "Yang", "Quanya", "", "Qiaoxue Wu",
#                        {},
#                        {},
#                        {},
#                        {})
# chihukuai = Character("",
#                        "Chi", "Shao", "Hukuai", "", "Rogue",
#                        {},
#                        {},
#                        {},
#                        {})
#fox girl character

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
    zhanjiuke.yournamelist = {-2:f'{player.surname} {player.courtname}', -1:f'{player.surname} {player.courtname}', 0:f'{player.surname} {player.courtname}', 1:player.courtname, 2:player.courtname, 3:f'{player.surname}-xiao{player.meiordi}', 4:f'{player.surname}-xiao{player.meiordi}', 5:f'{player.courtname1}-xiao{player.meiordi}', 6:f'{player.courtname1}-xiao{player.meiordi}', 7:f'{player.courtname1}-xiao{player.meiordi}', 8:f'{player.birthname}-xiao{player.meiordi}', 9:f'{player.birthname}-xiao{player.meiordi}', 10:f'A-{player.birthname}'}
    yongwenshi.yournamelist = {-2:f'{player.surname} {player.courtname}', -1:f'{player.surname} {player.courtname}', 0:f'{player.surname} {player.courtname}', 1:f'{player.courtname}', 2:f'{player.courtname}', 3:f'{player.courtname1}-{player.meiordi}', 4:f'{player.courtname1}-{player.meiordi}', 5:f'{player.surname} {player.birthname}', 6:f'{player.surname} {player.birthname}', 7:f'Xiao-{player.birthname}', 8:f'Xiao-{player.birthname}', 9:f'A-{player.birthname}', 10:f'A-{player.birthname}'}
    player.setsect(playersect, swordname, zhan_zhanmadao, sheng_hudiedao, yi_taijijian, yong_dadao, min_wodao, wu_hooksword, zhan_disc_robe, sheng_disc_robe, yi_disc_robe, yong_disc_robe, min_disc_robe, wu_disc_robe, zhanjiuke, yongwenshi, shengsulian)
    print(
     f'Your name is {player.surname} {player.birthname}, courtesy {player.courtname}. Your pronouns are {player.pronouns["subjprn"]}/{player.pronouns["objprn"]}/{player.pronouns["posadj"]}/{player.pronouns["posprn"]}/{player.pronouns["refprn"]}. Your elders may refer to you as {player.meiordi}{player.meiordi}. Your juniors may refer to you as {player.jieorge}{player.jieorge}. You are a {player.age} year old cultivator from the {player.sect} sect, and your sword is named {swordname}. You are in your room at Laolu inn in Baiping village on a mission to exorcise a vengeful ghost.')
    del swordname
    if input("Is this correct? (Yes/No): ") == "No":
     setinfo(player)

print("""
Welcome to Rolling Mists, Quiet Moons.
Rolling Mists, Quiet Moons is a text-based adventure developed in Python by Abigail Hui. It is set in fantastical ancient China. Previous knowledge of "xianxia" is strongly recommended but not required.
""")
ready = input("Please press enter when you are ready to begin the game. ")
if ready == "":
    print("Loading...")
print(start_room.getdescription(player))
print(
    "Your eyes flicker open slowly. You take a moment to gather yourself. As you blink away the haze of sleep, your memories come trickling back to you.")
setinfo(player)
Util.runact(player, qk_pouch, input(""))
