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
     self.earslots = 8
     self.neckslots = 5
     self.weaponslots = 2
     self.instrumentslots = 3
     self.ringslots = 10
     self.hairslots = 5
     self.wristslots = 8
     self.vambraces = None
     self.veil = None
     self.robe = None
     self.coat = None
     self.armor = None
     self.earrings = {}
     self.necklaces = {}
     self.weapons = {}
     self.instruments = {}
     self.rings = {}
     self.hairpins = {}
     self.bracelets = {}
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
     sep = ", "
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
             description += f'Inside it is{Util.getlistdescription(list(qk_pouch.contents.values()), qk_pouch)}. '
     description += f'You are wearing a {self.robe.itemname}.'
     if self.coat != None:
         description -= f'.'
         description += f' and a {self.coat.itemname}.'
     if self.coat != None:
         description += f' Covering your face is a {self.veil.itemname}.'
     if self.armor != None:
         description += f' Protecting you is a set of {self.armor.itemname}.'
     if self.vambraces != None:
         description += f' Over your robe is a pair of {self.vambraces.itemname}.'
     if self.earrings != {}:
         description += f' There are {Util.basiclistdescription(list(self.earrings.keys()))} on your ears.'
     if self.necklaces != {}:
         description += f' On your neck '
         if len(list(self.necklaces.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f' {Util.basiclistdescription(list(self.necklaces.keys()))}.'
     if self.weapons != {}:
         description += f' Strapped to your side '
         if len(list(self.weapons.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f' {Util.basiclistdescription(list(self.weapons.keys()))}.'
     if self.instruments != {}:
         description += f' Bound to your back '
         if len(list(self.instruments.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f' {Util.basiclistdescription(list(self.instruments.keys()))}.'
     if self.rings != {}:
         description += f' On your hand'
         if len(list(self.rings.keys())) == 1:
             description += f' is'
         else:
             description += f's are'
         description += f' {Util.basiclistdescription(list(self.rings.keys()))}.'
     if self.hairpins != {}:
         description += f' In your hair '
         if len(list(self.hairpins.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f' {Util.basiclistdescription(list(self.hairpins.keys()))}.'
     if self.bracelets != {}:
         description += f' Around your wrist'
         if len(list(self.necklaces.keys())) == 1:
             description += f' is'
         else:
             description += f's are'
         description += f' {Util.basiclistdescription(list(self.necklaces.keys()))}.'
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
 def wear(self, qk_pouch, item):
     reaction = ""
     if item in self.onplayer.values():
         return "You're already wearing that!"
     if item in qk_pouch.contents.values():
         match item.type:
             case "robe":
                 reaction = f'You slip out of your {self.robe} and into your {item.itemname}.'
                 qk_pouch.contents[self.robe.itemname] = self.robe
                 del self.onplayer[self.robe.itemname]
                 self.onplayer[item.itemname] = item
                 self.robe = item
             case "coat":
                 reaction = f'You shrug off your {self.coat} and put on your {item.itemname}.'
                 qk_pouch.contents[self.coat.itemname] = self.coat
                 del self.onplayer[self.coat.itemname]
                 self.onplayer[item.itemname] = item
                 self.coat = item
             case "veil":
                 reaction = f'You untie your {self.veil} and drape your {item.itemname} over your face.'
                 qk_pouch.contents[self.veil.itemname] = self.veil
                 del self.onplayer[self.veil.itemname]
                 self.onplayer[item.itemname] = item
                 self.veil = item
             case "armor":
                 reaction = f'You unattach your {self.armor} and heft on your {item.itemname}.'
                 qk_pouch.contents[self.armor.itemname] = self.armor
                 del self.onplayer[self.armor.itemname]
                 self.onplayer[item.itemname] = item
                 self.armor = item
             case "vambrace":
                 reaction = f'You take off your {self.vambraces} and strap on your {item.itemname}.'
                 qk_pouch.contents[self.vambraces.itemname] = self.vambraces
                 del self.onplayer[self.vambraces.itemname]
                 self.onplayer[item.itemname] = item
                 self.vambraces = item
             case "earring":
                 if self.earslots == 0:
                     reaction = "You don't have enough open piercings to wear that."
                 else:
                    reaction = f' You carefully fasten on your {item.itemname}.'
                    self.earslots -= 1
                    self.onplayer[item.itemname] = item
                    self.earrings[item.itemname] = item
             case "ring":
                 if self.ringslots == 0:
                     reaction = "You don't have enough space to wear that."
                 else:
                     reaction = f' You slide your {item.itemname} onto one of your fingers.'
                     self.ringslots -= 1
                     self.onplayer[item.itemname] = item
                     self.rings[item.itemname] = item
             case "bracelet":
                 if self.wristslots == 0:
                     reaction = "You don't have enough space to wear that."
                 else:
                     reaction = f' You slide your {item.itemname} around one of your wrists.'
                     self.wristslots -= 1
                     self.onplayer[item.itemname] = item
                     self.bracelets[item.itemname] = item
             case "hairpin":
                 if self.hairslots == 0:
                     reaction = "You don't have enough space to wear that."
                 else:
                     reaction = f' You slide your {item.itemname} into your hair.'
                     self.hairslots -= 1
                     self.onplayer[item.itemname] = item
                     self.hairpins[item.itemname] = item
             case "weapon":
                 if self.weaponslots == 0:
                     reaction = "You don't have enough space to wear that."
                 else:
                     reaction = f' You strap your {item.itemname} onto your side.'
                     self.weaponslots -= 1
                     self.onplayer[item.itemname] = item
                     self.weapons[item.itemname] = item
             case "instrument":
                 if self.instrumentslots == 0:
                     reaction = "You don't have enough space to wear that."
                 else:
                     reaction = f' You bind your {item.itemname} onto your back.'
                     self.instrumentslots -= 1
                     self.onplayer[item.itemname] = item
                     self.instruments[item.itemname] = item
             case other:
                 reaction = "You can't wear that!"
     else:
         reaction = "What are you trying to wear?"
     return reaction
 def undress(self, qk_pouch, item):
     reaction = ""
     if item in self.onplayer.values():
         match item.type:
             case "robe":
                 reaction = "You can't take that off."
             case "coat":
                 reaction = f'You shrug off your {self.coat}.'
                 qk_pouch.contents[self.coat.itemname] = self.coat
                 del self.onplayer[self.coat.itemname]
                 self.coat = None
             case "veil":
                 reaction = f'You untie your {self.veil}.'
                 qk_pouch.contents[self.veil.itemname] = self.veil
                 del self.onplayer[self.veil.itemname]
                 self.veil = None
             case "armor":
                 reaction = f'You unattach your {self.armor}.'
                 qk_pouch.contents[self.armor.itemname] = self.armor
                 del self.onplayer[self.armor.itemname]
                 self.armor = None
             case "vambrace":
                 reaction = f'You take off your {self.vambraces}.'
                 qk_pouch.contents[self.vambraces.itemname] = self.vambraces
                 del self.onplayer[self.vambraces.itemname]
                 self.vambraces = None
             case "earring":
                 reaction = f' You carefully unfasten your {item.itemname}.'
                 self.earslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.earrings[item.itemname]
             case "ring":
                 reaction = f' You slide your {item.itemname} off your finger.'
                 self.ringslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.rings[item.itemname]
             case "bracelet":
                 reaction = f' You slide your {item.itemname} off your wrist.'
                 self.wristslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.bracelets[item.itemname]
             case "hairpin":
                 reaction = f' You slide your {item.itemname} out of your hair.'
                 self.hairslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.hairpins[item.itemname]
             case "weapon":
                 reaction = f' You take your {item.itemname} off your side.'
                 self.weaponslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.weapons[item.itemname]
             case "instrument":
                 reaction = f' You take your {item.itemname} off your back.'
                 self.instrumentslots += 1
                 qk_pouch.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.instruments[item.itemname]
     else:
         reaction = "What are you trying to take off?"
     return reaction