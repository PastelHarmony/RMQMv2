from item import Item

class Player:
 def __init__(self):
     self.sect = ""
     self.sectcolors = ""
     self.sectsym = ""
     self.hasPouch = False
     self.onplayer = {}
 def getitem(self, qk_pouch, ex):
     if ex in qk_pouch.contents:
         item = qk_pouch.contents[ex]
     elif ex in self.onplayer:
         item = self.onplayer[ex]
     else:
         return None
     return item
 def setsect(self, sect):
     self.sect = sect
     if self.sect == "Yandi Zhan":
         self.sectcolors = "crimson"
         self.sectsym = "flame"
     elif self.sect == "Huangling Sheng":
         self.sectcolors = "golden"
         self.sectsym = "koi"
     elif self.sect == "Antian Yi":
         self.sectcolors = "sapphire"
         self.sectsym = "star"
     elif self.sect == "Jingnong Yong":
         self.sectcolors = "viridian"
         self.sectsym = "willow"
     elif self.sect == "Liangzi Min":
         self.sectcolors = "lilac"
         self.sectsym = "rose"
     elif self.sect == "Black Sect":
         self.sectcolors = "midnight black"
         self.sectsym = "raven"
 def takeitem(self, playloc, qk_pouch, item, container):
     if item == qk_pouch:
         del playloc.items[item.itemname]
         self.hasPouch = True
         return "You take the Qiankun pouch."
     elif self.hasPouch == False:
         return "You don't have anything to hold that item in."
     else:
         if item.canTake == False:
             return "You can't take that!"
         else:
             qk_pouch.contents[item.itemname] = item
             if item.isRegenerative == False:
                 item.amount[container] = item.amount[container] - 1
                 if item.amount[container] == 0:
                    del item.amount[container]
                    del container.items[item.itemname]
     try:
         item.amount[qk_pouch] = item.amount[qk_pouch] + 1
     except:
         item.amount[qk_pouch] = 1
     return f'You take the {item.itemname}.'