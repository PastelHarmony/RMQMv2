from item import Item
from util import Util

class Player:
 def __init__(self):
     self.playloc = None
     self.surname = ""
     self.birthname = ""
     self.courtname = ""
     self.courtname1 = ""
     self.courtname2 = ""
     self.title = None
     self.pronouns = {}
     self.isorare = ""
     self.meiordi = ""
     self.jieorge = ""
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
 def setcourtname(self):
     self.courtname = self.courtname1 + self.courtname2.lower()
 def setprn(self, prn, honorifics):
     if prn == "she/her":
         self.pronouns["subjprn"] = "she"
         self.pronouns["objprn"] = "her"
         self.pronouns["posadj"] = "her"
         self.pronouns["posprn"] = "hers"
         self.pronouns["refprn"] = "herself"
         self.isorare = "is"
     elif prn == "he/him":
         self.pronouns["subjprn"] = "he"
         self.pronouns["objprn"] = "him"
         self.pronouns["posadj"] = "his"
         self.pronouns["posprn"] = "his"
         self.pronouns["refprn"] = "himself"
         self.isorare = "is"
     elif prn == "they/them":
         self.pronouns["subjprn"] = "they"
         self.pronouns["objprn"] = "them"
         self.pronouns["posadj"] = "their"
         self.pronouns["posprn"] = "theirs"
         self.pronouns["refprn"] = "themselves"
         self.isorare = "are"
     elif prn == "it/its":
         self.pronouns["subjprn"] = "it"
         self.pronouns["objprn"] = "it"
         self.pronouns["posadj"] = "its"
         self.pronouns["posprn"] = "its"
         self.pronouns["refprn"] = "itself"
         self.isorare = "is"
     elif prn == "other":
         self.pronouns["subjprn"] = input("What are your subjective pronouns?")
         self.pronouns["objprn"] = input("What are your objective pronouns")
         self.pronouns["posadj"] = input("What are your possessive adjectives?")
         self.pronouns["posprn"] = input("What are your posessive pronouns?")
         self.pronouns["refprn"] = input("What are your reflexive pronouns?")
         self.isorare = input("Do your pronouns refer to yourself as 'is' or 'are'? (Ex: 'She is' vs. 'They are'): ")
     if honorifics == "1":
         self.meiordi = "mei"
         self.jieorge = "jie"
     elif honorifics == "2":
         self.meiordi = "di"
         self.jieorge = "ge"
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
 def takeitem(self, qk_pouch, item, container):
     if item == qk_pouch:
         del self.playloc.items[item.itemname]
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
 def getdescription(self, qk_pouch):
     description = f'Your given name is {self.surname} {self.birthname}. Your courtesy name is {self.surname} {self.courtname}. '
     if self.title != None:
         description += f'Your title is {self.title}. '
     description += f'Your pronouns are {self.pronouns["subjprn"]}/{self.pronouns["objprn"]}. You are in the {self.sect} sect. '
     if self.hasPouch == False:
         description += "You are not carrying anything. "
     else:
         description += "You are carrying a Qiankun pouch. "
         if qk_pouch.contents == {}:
             description += "There is nothing in the Qiankun pouch. "
         else:
             description += f'Inside it is {Util.getlistdescription(list(qk_pouch.contents.values()), qk_pouch)}. '
     description += f'You are wearing {Util.getlistdescription(list(self.onplayer.values()), qk_pouch)}.'
     return description
 def eat(self, qk_pouch, item):
     item.amount[qk_pouch] -= 1
     if item.amount[qk_pouch] == 0:
         del item.amount[qk_pouch]
         del qk_pouch.contents[item.itemname]
     return f'You eat the {item.itemname}.'
 def go(self, time, direction):
     try:
         newroom = self.playloc.connects[direction]
         return [newroom.getdescription(time), newroom]
     except:
         return ["That area hasn't been developed yet!", self.playloc]
 def put(self, qk_pouch, itemname, where):
     try:
         item = qk_pouch.contents[itemname]
     except:
         return "You don't have that item. (Tip: The item needs to be in your pouch)"
     if where == "down":
         try:
             item.amount[self.playloc] += 1
         except:
             self.playloc.items[itemname] = item
             item.amount[self.playloc] = 1
         item.amount[qk_pouch] -= 1
         if item.amount[qk_pouch] == 0:
            del qk_pouch.contents[item.itemname]
            del item.amount[qk_pouch]
         return f'You put down 1 {item.itemname}.'
     else:
         container = Util.getitemfromunknown(self, None, where)[0]
         if container == None:
             return "Where do you want to put that?"
         try:
             item.amount[container] += 1
         except:
             container.contents[itemname] = item
             item.amount[container] = 1
         item.amount[qk_pouch] -= 1
         if item.amount[qk_pouch] == 0:
             del qk_pouch.contents[item.itemname]
             del item.amount[qk_pouch]
         return f'You put 1 {item.itemname} {container.inoron} the {container.itemname}.'
 def push(self, item):
     if item.canPush == False:
         return f'You try to push the {item.itemname} but it doesn\'t budge.'
     match item:
         case 0:
             return "hi"
         case other:
            return f'You push the {item.itemname} around. It doesn\'t do much.'