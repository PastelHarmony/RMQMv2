from item import Item

class Player:
 def __init__(self):
     self.sect = ""
     self.sectcolors = ""
     self.sectsym = ""
     self.inv = {}
     self.onplayer = {}
 def getitem(self, ex):
     if ex in self.inv:
         item = self.inv[ex]
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