from item import Item
from util import Util

class Player:
 def __init__(self):
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
             description += f'Inside it is {Util.getlistdescription(list(qk_pouch.contents.keys()))}. '
     description += f'You are wearing {Util.getlistdescription(list(self.onplayer.keys()))}.'
     return description