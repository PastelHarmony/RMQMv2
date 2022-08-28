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
     self.sectstatus = "disciple"
     self.quests = {}
     # social score = charisma + answer + status
     self.stats = {"max health":100, "health":100, "strength":0, "cultivation":0, "physical defense":0, "spiritual defense":0, "fire resistance":0, "poison resistance":0, "dexterity":0, "charisma":0, "intelligence":0}
     self.skills = {"bladework":(0, 0), "archery":(0, 0), "spears":(0, 0), "battleaxe":(0, 0), "clubbing":(0, 0), "unarmed combat":(0, 0), "talismans":(0, 0), "healing":(0, 0), "botany":(0, 0), "fishing":(0, 0), "cooking":(0, 0), "logging":(0, 0), "mining":(0, 0), "forging":(0, 0), "communication":(0, 0)}
     self.afflictions = []
     self.incombat = False
     self.spawnpoint = None
     self.inv = None
     self.money = 140
     self.age = 21
     self.days = 0
     self.time = "day"
     self.weather = "clear"
 def getitem(self, ex):
     if ex in self.inv.contents:
         item = self.inv.contents[ex]
     elif ex in self.onplayer:
         item = self.onplayer[ex]
     else:
         return None
     return item
 def setprn(self, prn):
     match prn:
         case "she/her":
             self.pronouns["subjprn"] = "she"
             self.pronouns["objprn"] = "her"
             self.pronouns["posadj"] = "her"
             self.pronouns["posprn"] = "hers"
             self.pronouns["refprn"] = "herself"
             self.isorare = "is"
         case "he/him":
             self.pronouns["subjprn"] = "he"
             self.pronouns["objprn"] = "him"
             self.pronouns["posadj"] = "his"
             self.pronouns["posprn"] = "his"
             self.pronouns["refprn"] = "himself"
             self.isorare = "is"
         case "they/them":
             self.pronouns["subjprn"] = "they"
             self.pronouns["objprn"] = "them"
             self.pronouns["posadj"] = "their"
             self.pronouns["posprn"] = "theirs"
             self.pronouns["refprn"] = "themselves"
             self.isorare = "are"
         case "it/its":
             self.pronouns["subjprn"] = "it"
             self.pronouns["objprn"] = "it"
             self.pronouns["posadj"] = "its"
             self.pronouns["posprn"] = "its"
             self.pronouns["refprn"] = "itself"
             self.isorare = "is"
         case "other":
             self.pronouns["subjprn"] = input("What are your subjective pronouns?")
             self.pronouns["objprn"] = input("What are your objective pronouns")
             self.pronouns["posadj"] = input("What are your possessive adjectives?")
             self.pronouns["posprn"] = input("What are your posessive pronouns?")
             self.pronouns["refprn"] = input("What are your reflexive pronouns?")
             self.isorare = input("Do your pronouns refer to yourself as 'is' or 'are'? (Ex: 'She is' vs. 'They are'): ")
         case other:
             self.setprn(input("Please input a valid pronoun set. "))
 def sethonorific(self, honorifics):
     if honorifics == "1":
         self.meiordi = "mei"
         self.jieorge = "jie"
     elif honorifics == "2":
         self.meiordi = "di"
         self.jieorge = "ge"
     else:
         self.sethonorific(input("Please input a valid number (1 or 2). "))

 def setsect(self, sect, swordname, zhanmadao, hudiedao, taijijian, dadao, wodao, hooksword, zhanrobe, shengrobe, yirobe, yongrobe, minrobe, wurobe):
     self.sect = sect
     match sect:
         case "Yandi Zhan":
             self.sectcolors = "crimson"
             self.sectsym = "flame"
             self.weapons[swordname] = zhanmadao
             self.onplayer[zhanrobe.itemname] = zhanrobe
             self.robe = zhanrobe
             # self.spawnpoint = zhan_clinic_room1
         case "Huangling Sheng":
             self.sectcolors = "golden"
             self.sectsym = "koi"
             self.weapons[swordname] = hudiedao
             self.onplayer[shengrobe.itemname] = shengrobe
             self.robe = shengrobe
             # self.spawnpoint = sheng_clinic_room1
         case "Antian Yi":
             self.sectcolors = "sapphire"
             self.sectsym = "star"
             self.weapons[swordname] = taijijian
             self.onplayer[yirobe.itemname] = yirobe
             self.robe = yirobe
             # self.spawnpoint = yi_clinic_room1
         case "Jingnong Yong":
             self.sectcolors = "viridian"
             self.sectsym = "willow"
             self.weapons[swordname] = dadao
             self.onplayer[yongrobe.itemname] = yongrobe
             self.robe = yongrobe
             # self.spawnpoint = yong_clinic_room1
         case "Liangzi Min":
             self.sectcolors = "lilac"
             self.sectsym = "rose"
             self.weapons[swordname] = wodao
             self.onplayer[minrobe.itemname] = minrobe
             self.robe = minrobe
             # self.spawnpoint = min_clinic_room1
         case "Qiaoxue Wu":
             self.sectcolors = "onyx"
             self.sectsym = "raven"
             self.weapons[swordname] = hooksword
             self.onplayer[wurobe.itemname] = wurobe
             self.robe = wurobe
             # self.spawnpoint = wu_clinic_room1
         case other:
             self.setsect(input("Please select a valid sect. ").title(), swordname, zhanmadao, hudiedao, taijijian, dadao, wodao, hooksword, zhanrobe, shengrobe, yirobe, yongrobe, minrobe, wurobe)
     self.robe.amount[self] = 1
     self.weapons[swordname].amount[self] = 1
     self.weapons[swordname].itemname = swordname
     self.onplayer[swordname] = self.weapons[swordname]
 def takeitem(self, qk_pouch, item, container):
     if item == qk_pouch:
         del self.playloc.items[item.itemname]
         self.hasPouch = True
         self.inv = qk_pouch
         return "You take the Qiankun pouch."
     elif self.hasPouch == False:
         return "You don't have anything to hold that item in."
     else:
         if item.canTake == False:
             return "You can't take that!"
         else:
             if item.isLiquid == True:
                 return "You can't take that, it's liquid. First put it in a container."
             else:
                 amount = Util.getamount(container, item, "take")
                 if amount == 0:
                     return f'You don\'t take any {item.pluralitemname}.'
                 self.inv.contents[item.itemname] = item
                 if item.isRegenerative == False:
                     item.amount[container] = item.amount[container] - 1
                     if item.amount[container] == 0:
                        del item.amount[container]
                        del container.items[item.itemname]
     try:
         item.amount[self.inv] = item.amount[self.inv] + 1
     except:
         item.amount[self.inv] = 1
     return f'You take the {item.itemname}.'
 def getdescription(self):
     description = f'Your given name is {self.surname} {self.birthname}. Your courtesy name is {self.surname} {self.courtname}. You are {self.age} years old.'
     if self.title != None:
         description += f'Your title is {self.title}. '
     description += f'Your pronouns are {self.pronouns["subjprn"]}/{self.pronouns["objprn"]}. You are in the {self.sect} sect. '
     description += f'You have {self.money} yuan. '
     if self.hasPouch == False:
         description += "You are not carrying anything. "
     else:
         description += "You are carrying a Qiankun pouch. "
         if self.inv.contents == {}:
             description += "There is nothing in the Qiankun pouch. "
         else:
             description += f'Inside it is{Util.getlistdescription(list(self.inv.contents.values()), self.inv)}. '
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
         description += f' There are{Util.basiclistdescription(list(self.earrings.values()))} on your ears.'
     if self.necklaces != {}:
         description += f' On your neck '
         if len(list(self.necklaces.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f'{Util.getlistdescription(list(self.necklaces.values()), self.playloc)}.'
     if self.weapons != {}:
         description += f' Strapped to your side '
         if len(list(self.weapons.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f'{Util.basiclistdescription(list(self.weapons.values()))}.'
     if self.instruments != {}:
         description += f' Bound to your back '
         if len(list(self.instruments.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f'{Util.basiclistdescription(list(self.instruments.values()))}.'
     if self.rings != {}:
         description += f' On your hand'
         if len(list(self.rings.keys())) == 1:
             description += f' is'
         else:
             description += f's are'
         description += f'{Util.getlistdescription(list(self.rings.values()), self.playloc)}.'
     if self.hairpins != {}:
         description += f' In your hair '
         if len(list(self.hairpins.keys())) == 1:
             description += f'is'
         else:
             description += f'are'
         description += f'{Util.getlistdescription(list(self.hairpins.values()), self.playloc)}.'
     if self.bracelets != {}:
         description += f' Around your wrist'
         if len(list(self.necklaces.keys())) == 1:
             description += f' is'
         else:
             description += f's are'
         description += f'{Util.getlistdescription(list(self.necklaces.values()), self.playloc)}.'
     return description
 def eat(self, item):
     amount = Util.getamount(self.inv, item, "eat")
     item.amount[self.inv] -= amount
     if item.amount[self.inv] == 0:
         del item.amount[self.inv]
         del self.inv.contents[item.itemname]
     if amount == 1:
        return f'You eat the {item.itemname}.'
     else:
         return f'You eat {amount} {item.pluralitemname}.'
 def go(self, direction):
     try:
         newroom = self.playloc.connects[direction]
         for creature in self.playloc.npcs.values():
             creature.stats["health"] = creature.stats["max health"]
             if creature.isPassive == True:
                 creature.isHostile = False
         return [newroom.getdescription(self), newroom]
     except:
         return ["That area hasn't been developed yet!", self.playloc]
 def put(self, itemname, where):
     if itemname == "Qiankun pouch":
         if where == "down":
             self.inv.amount[self.playloc] += 1
             self.playloc.items[self.inv.itemname] = self.inv
             self.inv = None
             self.hasPouch = False
             return f'You put the Qiankun pouch down.'
         else:
             container = Util.getitemfromunknown(self, None, where)[0]
             self.inv.amount[container] += 1
             container.contents[self.inv.itemname] = self.inv
             self.inv = None
             self.hasPouch = False
             return f'You put the Qiankun pouch {container.inoron} the {container.itemname}.'
     try:
         item = self.inv.contents[itemname]
     except:
         return "You don't have that item. (Tip: The item needs to be in your pouch)"
     if where == "down":
         amount = Util.getamount(self.inv, item, "put")
         try:
             item.amount[self.playloc] += amount
         except:
             self.playloc.items[itemname] = item
             item.amount[self.playloc] = amount
         item.amount[self.inv] -= amount
         if item.amount[self.inv] == 0:
            del self.inv.contents[item.itemname]
            del item.amount[self.inv]
         if item == self.inv:
             self.inv = None
         if amount == 1:
            return f'You put down 1 {item.itemname}.'
         else:
             return f'You put down {amount} {item.pluralitemname}.'
     else:
         container = Util.getitemfromunknown(self, None, where)[0]
         amount = Util.getamount(self.inv, item, "put")
         if container == None:
             return "Where do you want to put that?"
         try:
             item.amount[container] += amount
         except:
             container.contents[itemname] = item
             item.amount[container] = amount
         item.amount[self.inv] -= amount
         if item.amount[self.inv] == 0:
             del self.inv.contents[item.itemname]
             del item.amount[self.inv]
             if item == self.inv:
                 self.inv = None
         if amount == 1:
            return f'You put 1 {item.itemname} {container.inoron} the {container.itemname}.'
         else:
             return f'You put {amount} {item.pluralitemname} {container.inoron} the {container.itemname}.'
 def wear(self, item):
     reaction = ""
     if item in self.onplayer.values():
         return "You're already wearing that!"
     if item in self.inv.contents.values():
         match item.type:
             case "robe":
                 reaction = f'You slip out of your {self.robe} and into your {item.itemname}.'
                 self.inv.contents[self.robe.itemname] = self.robe
                 del self.onplayer[self.robe.itemname]
                 self.onplayer[item.itemname] = item
                 self.robe = item
             case "coat":
                 reaction = f'You shrug off your {self.coat} and put on your {item.itemname}.'
                 self.inv.contents[self.coat.itemname] = self.coat
                 del self.onplayer[self.coat.itemname]
                 self.onplayer[item.itemname] = item
                 self.coat = item
             case "veil":
                 reaction = f'You untie your {self.veil} and drape your {item.itemname} over your face.'
                 self.inv.contents[self.veil.itemname] = self.veil
                 del self.onplayer[self.veil.itemname]
                 self.onplayer[item.itemname] = item
                 self.veil = item
             case "armor":
                 reaction = f'You unattach your {self.armor} and heft on your {item.itemname}.'
                 self.inv.contents[self.armor.itemname] = self.armor
                 del self.onplayer[self.armor.itemname]
                 self.onplayer[item.itemname] = item
                 self.armor = item
             case "vambrace":
                 reaction = f'You take off your {self.vambraces} and strap on your {item.itemname}.'
                 self.inv.contents[self.vambraces.itemname] = self.vambraces
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
 def undress(self, item):
     reaction = ""
     if item in self.onplayer.values():
         match item.type:
             case "robe":
                 reaction = "You can't take that off."
             case "coat":
                 reaction = f'You shrug off your {self.coat}.'
                 self.inv.contents[self.coat.itemname] = self.coat
                 del self.onplayer[self.coat.itemname]
                 self.coat = None
             case "veil":
                 reaction = f'You untie your {self.veil}.'
                 self.inv.contents[self.veil.itemname] = self.veil
                 del self.onplayer[self.veil.itemname]
                 self.veil = None
             case "armor":
                 reaction = f'You unattach your {self.armor}.'
                 self.inv.contents[self.armor.itemname] = self.armor
                 del self.onplayer[self.armor.itemname]
                 self.armor = None
             case "vambrace":
                 reaction = f'You take off your {self.vambraces}.'
                 self.inv.contents[self.vambraces.itemname] = self.vambraces
                 del self.onplayer[self.vambraces.itemname]
                 self.vambraces = None
             case "earring":
                 reaction = f' You carefully unfasten your {item.itemname}.'
                 self.earslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.earrings[item.itemname]
             case "ring":
                 reaction = f' You slide your {item.itemname} off your finger.'
                 self.ringslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.rings[item.itemname]
             case "bracelet":
                 reaction = f' You slide your {item.itemname} off your wrist.'
                 self.wristslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.bracelets[item.itemname]
             case "hairpin":
                 reaction = f' You slide your {item.itemname} out of your hair.'
                 self.hairslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.hairpins[item.itemname]
             case "weapon":
                 reaction = f' You take your {item.itemname} off your side.'
                 self.weaponslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.weapons[item.itemname]
             case "instrument":
                 reaction = f' You take your {item.itemname} off your back.'
                 self.instrumentslots += 1
                 self.inv.contents[item.itemname] = item
                 del self.onplayer[item.itemname]
                 del self.instruments[item.itemname]
     else:
         reaction = "What are you trying to take off?"
     return reaction

 def push(self, item):
    try:
        print(item)
        if item.canPush == False:
            return f'You try to push the {item.itemname} but it doesn\'t budge.'
        match item.itemname and self.playloc.loc and self.playloc.subloc:
            case "window" | "Laolu Inn" | "Your Room":
                return "hi"
            case other:
                return f'You push the {item.itemname} around. It doesn\'t do much.'
    except:
        return "What are you trying to push?"

 def useitem(self, itema, itemb):
    if itema.isCrafter == True and isinstance(itemb, str):
       return self.craft(itema)
    if itema.type == "bed":
        if self.time == "night" and self.incombat == False:
            return self.sleep()
        else:
            return "You can't sleep right now."
    if itemb == "":
        return "What do you want to use this item with?"
    if isinstance(itema, str) or isinstance(itemb, str):
        return "You don't have that item."
    if itema.isTool == True:
        return self.usetool(itema, itemb)
    elif itemb.isTool == True:
        return self.usetool(itemb, itema)
    if itema.type == "talisman":
        try:
            isCreature = itemb.drops
            return self.usetalismanoncreature(itema, itemb)
        except:
            try:
                isItem = itemb.canTake
                return self.usetalismanonobject(itema, itemb)
            except:
                return "You cannot use a talisman on that."
    elif itemb.type == "talisman":
        try:
            isCreature = itema.drops
            return self.usetalismanoncreature(itemb, itema)
        except:
            try:
                isItem = itema.canTake
                return self.usetalismanonobject(itemb, itema)
            except:
                return "You cannot use a talisman on that."
    match itema.itemname and itemb.itemname:
        case "apple" | "pear":
            return "hi"
    return "Those items don't do anything together."

 def sleep(self):
    self.time = "day"
    return f'You slept.\nIt is now {self.time}. You have been in Rolling Mists, Quiet Moons for {self.days} days.'

 def rest(self):
     self.time = "night"
     return f'You rested until it was {self.time}.'

 def usetalismanoncreature(self, talisman, creature):
     match talisman.itemname:
         case "freezing talisman":
             if "frozen" in creature.afflictions:
                 return f'This {creature.name} is already frozen.'
             elif "wet" in creature.afflictions or creature.isLiquid == True:
                 self.skills["talismans"] += 10 * (1 + self.stats["intelligence"] / 100)
                 # remove "wet"
                 creature.afflictions.append("frozen")
                 return f'You froze the {creature.name}.'
             elif "burning" in creature.afflictions:
                 self.skills["talismans"] += 10 * (1 + self.stats["intelligence"] / 100)
                 # remove "burning"
                 return f'The cold put out the fire on the {creature.name}.'
             else:
                 return f'You use the freezing talisman, but the {creature.name} shakes it off.'
         case "water talisman":
             if "wet" in creature.afflictions or creature.isLiquid == True:
                 return f'The {creature.name} is already wet.'
             elif "wet" not in creature.afflictions and creature.isLiquid == False:
                self.skills["talismans"] += 10 * (1 + self.stats["intelligence"]/100)
                creature.afflictions.append("wet")
                if "burning" in creature.afflictions:
                    # remove "burning"
                    return f'The water put out the fire on the {creature.name}.'
                return f'You splashed water on the {creature.name}.'
         case "burning talisman":
             if "burning" in creature.afflictions:
                 return f'This {creature.name} is already on fire.'
             elif creature.isLiquid == True:
                 self.skills["talismans"] += 10 * (1 + self.stats["intelligence"] / 100)
                 tempmsg = f'You vaporized the {creature.name}, dealing {creature.stats["health"] * .1} points of damage.'
                 creature.stats["health"] = creature.stats["health"] * .9
                 return tempmsg
             elif "wet" in creature.afflictions:
                 self.skills["talismans"] += 10 * (1 + self.stats["intelligence"] / 100)
                 return f'The fire vaporized the water off of the {creature.name}.'
             elif "frozen" in creature.afflictions:
                 self.skills["talismans"] += 10 * (1 + self.stats["intelligence"] / 100)
                 # remove "frozen
                 tempmsg = f'You melted the {creature.name}, dealing {creature.stats["health"] * .1} points of damage.'
                 creature.stats["health"] = creature.stats["health"] * .9
                 return tempmsg
         case other:
             return

 def usetalismanonobject(self, talisman, object):
     match talisman.itemname:
         case "freezing talisman":
             return
         case "water talisman":
             return
         case "burning talisman":
             return
         case other:
             return

 def usetool(self, tool, item):
     match tool.type:
         case "axe":
             return f'{item} go chop chop make wood'
         case "knife":
             return f'{item}'
         case "pickaxe":
             return
         case "writer":
             return "do you wanna draw or write"
         case other:
             return "Those items don't do anything together."
 def craft(self, crafter):
     match crafter.type:
         case "forge":
             return self.forge(crafter)
         case "cooker":
             return self.cook(crafter)
         case other:
             return f'The items in the {crafter.itemname} do not do anything together.'

 def forge(self, forge):
     return

 def cook(self, cooker):
     return

 def attack(self, creature, weapon):
     msg = ""
     dodge = Util.chance(creature.stats["dodge"])
     if dodge == True:
         return f'The {creature.name} dodged and took no damage.'
     if weapon == "self":
         dmg = self.stats["strength"] + (self.skills["unarmed combat"] * 10)
         creature.stats["health"] -= dmg
         msg = f'You hit the {creature.name} and dealt {self.stats["strength"]} damage.'
     else:
         match weapon.type:
             case "sword":
                 self.skills["bladework"][1] += 10 * (1 + self.stats["intelligence"]/100)
                 dmg = self.skills["bladework"][0] * 15 + self.skills["battleaxe"][0]**2
             case "bow":
                 self.skills["archery"][1] += 10 * (1 + self.stats["intelligence"] / 100)
                 dmg = self.skills["archery"][0] * 15 + self.skills["battleaxe"][0]**2
             case "spear":
                self.skills["spears"][1] += 10 * (1 + self.stats["intelligence"] / 100)
                dmg = self.skills["spears"][0] * 15 + self.skills["battleaxe"][0]**2
             case "club":
                 self.skills["clubbing"][1] += 10 * (1 + self.stats["intelligence"] / 100)
                 dmg = self.skills["clubbing"][0] * 15 + self.skills["battleaxe"][0]**2
             case "battleaxe":
                 self.skills["battleaxe"][1] += 10 * (1 + self.stats["intelligence"] / 100)
                 dmg = self.skills["battleaxe"][0] * 15 + self.skills["battleaxe"][0]**2
             case other:
                 print("There is a bug. Weapon type not found.")
                 dmg = 0
         physdmg = weapon.bluntdmg*self.stats["strength"] + weapon.precdmg*self.stats["dexterity"] - creature.stats["physical defense"]
         if physdmg <0: physdmg = 0
         magicdmg = weapon.spiritdmg["cultivation"] - creature.stats["spiritual defense"]
         if magicdmg<0: magicdmg = 0
         dmg += physdmg+magicdmg
         creature.stats["health"] -= dmg
         msg += f' You attacked the {creature.name} with your {weapon.itemname} and dealt {dmg} damage.'
     if creature.stats["health"] <=0:
        msg += f' {self.kill(creature)}'
     else:
         msg += f' It has {creature.stats["health"]} hit points left.'
     return msg

 def kill(self, creature):
     loot = []
     for item in creature.drops.keys():
         loot.append(item)
         if item not in self.playloc.items.values():
             self.playloc.items.values[item.itemname] = item
             item.amount[self.playloc] = creature.drops[item]
         else:
             item.amount[self.playloc] += creature.drops[item]
     killmsg = f'You slayed the {creature.name}.'
     if loot != []:
         killmsg += f' It dropped{Util.getlistdescription(loot, self.playloc)}.'
     else:
         killmsg += f' It dropped nothing.'
     return killmsg

 def die(self):
     self.incombat = False
     for creature in self.playloc.npcs:
         if creature.isPassive == True:
             creature.isHostile = False
     self.playloc = self.spawnpoint
     msg = "You fainted!"
     msg += f'\n{self.playloc.getdescription(self)}'
     return msg
