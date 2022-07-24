from player import Player
from room import Room
from item import Item

def runact(action):
 if "examine" == action[:7]:
  itemname = action[8:]
  examine(itemname)
 else:
  print("What are you trying to do?")
 runact(input(""))

def examine(itemname):
 item = None
 if itemname in playloc.items or itemname in playloc.hidden_items:
  item = playloc.getitem(itemname)
 elif itemname in player.inv or itemname in player.onplayer:
  item = player.getitem(itemname)
 if item is None:
  print("What are you trying to examine?")
 else:
  print(item.examineitem(player))

player = Player()

brick = Item("brick", "A red brick", "misc", False, None, None, None)
qk_pouch = Item("Qiankun pouch", f'A small {player.sectcolors} bag made of thick silk. It is secured with a silver drawstring and embroidered with intricate {player.sectsym}s. It can hold an unlimited amount of objects.', "container", True, {}, False, "in")

start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.", "Silver moonlight gently brushes along the walls.", "The pattering of the rain echoes loudly through the dim room.", "Snow twirls outside the window, blowing wildly in the wind.", "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.", {brick.itemname:brick, qk_pouch.itemname:qk_pouch}, {}, {})
playloc = start_room

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
playersect = input("""What sect are you from?
Yandi Zhan - The Zhan sect is an extensive militaristic sect located in the forests below the Huangling Sheng. It is also bordered by the Antian Yi and Liangzi Min to the west and by the Jingnong Yong and Qiaoxue Wu to the east. Below it lies the ocean.
Huangling Sheng - The Sheng sect is a fairly large sect with a prosperous trading economy. It is located near a snowy mountain range that feeds into many large rivers and bordered below by the Yandi Zhang, the Antian Yi, and the Jingnong Yong. Its east side reaches the sea.
Antian Yi - The Yi sect is a moderately small but widely influential sect that focuses on self-enlightenment and justice. It is bordered on the north by the Huangling Sheng, on the south by the Liangzi Min, and to the east by the Yandi Zhang. It is also known for its beautiful waterfalls.
Jingnong Yong - The Yong sect is a wide agricultural sect in the plains below the Huangling Sheng and to the east of the Yandi Zhan. Its people are known to be diligent and hard-working. Below it lies the Qiaoxue Wu.
Liangzi Min - The Min sect is a scholarly sect of intermediate size with rolling hills and sparkling lakes fed by the many bays below it. It is bordered by the Antian Yi on the north and the Yandi Zhang on the east.
Qiaoxue Wu - The Wu sect is on the smaller side, but it is one of the oldest that still exists. It has magnificent cave systems and shadowy forests. It is also heavily shrouded in mystery; Despite this, it is known for producing great works of art. It is located to the south of the Jingnong Yong and to the east of the Yandi Zhan.
(Please reply with full sect name. Capitalization is important): """)
player.setsect(playersect)
runact(input(""))