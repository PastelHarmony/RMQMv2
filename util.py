from random import randint


class Util():
    @staticmethod
    def getlistdescription(listofitems, location):
        list = ""
        if len(listofitems) == 1:
            word = listofitems[0].itemname
            if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
                list += f' an {word}'
            else:
                list += f' a {word}'
            return list
        else:
            for i in range(len(listofitems)):
                word = listofitems[i].itemname
                if i != 0 and len(listofitems) > 2:
                    list += ","
                if i == len(listofitems)-1:
                    list += " and"
                if listofitems[i].amount[location] > 1:
                    list += f' {listofitems[i].amount[location]} {word}s'
                elif word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
                    list += f' an {word}'
                else:
                    list += f' a {word}'
        return list
    @staticmethod
    def basiclistdescription(listofitems):
        list = ""
        if len(listofitems) == 1:
            return f' {listofitems[0].itemname}'
        for i in range(len(listofitems)):
            word = listofitems[i].itemname
            if i != 0 and len(listofitems) > 2:
                list += ","
            if i == len(listofitems) - 1:
                list += " and"
            list += f' {word}'
        return list

    @staticmethod
    def runact(player, qk_pouch, action):
        try:
            if "examine" == action[:7]:
                itemname = action[8:]
                if " in " in action:
                    arr = itemname.split(" in ")
                    itemname = arr[0]
                    containername = arr[1]
                if " from " in action:
                    arr = itemname.split(" from ")
                    itemname = arr[0]
                    containername = arr[1]
                else:
                    containername = None
                print(Util.examine(player, itemname, containername))
            elif "use" == action[:3]:
                item = action[4:]
                if " with " in item:
                    arr = item.split(" with ")
                    a = arr[0]
                    b = arr[1]
                elif " on " in item:
                    arr = item.split(" on ")
                    a = arr[0]
                    b = arr[1]
                elif " and " in item:
                    arr = item.split(" and ")
                    a = arr[0]
                    b = arr[1]
                else:
                    a = item
                    b = ""
                itema = Util.getitemfromfree(player, a)[1]
                itemb = Util.getitemfromfree(player, b)[1]
                print(player.useitem(itema, itemb))
            elif "go" == action[:2]:
                arr = player.go(action[3:])
                print(arr[0])
                player.playloc = arr[1]
            elif "inv" == action:
                description = Util.examine(player, "self", None)
                newdesc = description.split(". ")
                print(". ".join(newdesc[4:]))
            elif "take" == action[:4]:
                itemname = action[5:]
                if " from " in itemname:
                    arr = itemname.split(" from ")
                    itemname = arr[0]
                    containername = arr[1]
                else:
                    containername = None
                print(Util.take(player, qk_pouch, itemname, containername))
            elif "eat" == action[:3]:
                try:
                    try:
                        arr = action[4:].split(" in ")
                        itemname = arr[0]
                        containername = arr[1]
                        Util.take(player, qk_pouch, itemname, containername)
                    except:
                        itemname = action[4:]
                        try:
                            item = player.inv.contents[itemname]
                        except:
                            item = player.playloc.items[itemname]
                    item = player.inv.contents[itemname]
                    if item.type == "food":
                        print(player.eat(player.inv, item))
                    else:
                        print("You can't eat that.")
                except:
                    print("What are you trying to eat?")
            elif "put" == action[:3]:
                if "down" in action[4:]:
                    arr = action.split(" down ")
                    itemname = arr[1]
                    containername = "down"
                    print(player.put(itemname, containername))
                else:
                    try:
                        arr = action[4:].split(" in ")
                        itemname = arr[0]
                        containername = arr[1]
                        print(player.put(player.inv, itemname, containername))
                    except:
                        try:
                            arr = action[4:].split(" on ")
                            itemname = arr[0]
                            containername = arr[1]
                            print(player.put(player.inv, itemname, containername))
                        except:
                            print("Where are you trying to put that?")
            elif "push" == action[:4]:
                item = Util.getitemfromunknown(player, None, action[5:])[0]
                print(player.push(item))
            elif "wear" == action[:4]:
                item = Util.getitemfromunknown(player, None, action[5:])[0]
                print(player.wear(player.inv, item))
            elif "undress" == action[:7]:
                item = player.onplayer[action[8:]]
                print(player.undress(player.inv, item))
            elif "change" == action[:5]:
                print(Util.changeinfo(player, action[6:]))
            elif "rename" == action[:6]:
                print(Util.rename(player, action[7:]))
            elif "attack" == action[:6]:
                try:
                    arr = action[7:].split(" with ")
                    try:
                        creature = player.playloc.npcs[arr[0]]
                        try:
                            weapon = player.weapons[arr[1]]
                            creature.isHostile = True
                            player.inCombat = True
                            print(player.attack(creature, weapon))
                        except:
                            try:
                                weapon = player.instruments[arr[1]]
                                creature.isHostile = True
                                player.inCombat = True
                                print(player.attack(creature, weapon))
                            except:
                                print("What are you trying to attack the creature with?")
                    except:
                        print("What are you trying to attack?")
                except:
                    print(f'What are you trying to attack the creature with?')
            elif action == "rest":
                if player.time == "day" and player.incombat == False:
                    print(player.rest())
                elif player.time == "night" and player.incombat == False:
                    print(player.sleep())
                else:
                    print("You cannot rest right now.")
            elif "plant" == action[:5]:
                plantname = action[6:]
                try:
                    plant = player.inv[plantname]
                    if plant.canPlant == True:
                        print(player.plant(plant))
                    else:
                        print("You can't plant that.")
                except:
                    print("What are you trying to plant?")
                return
            else:
                print("What are you trying to do?")
        except:
            print("Could not perform that action. (Hint: You must be carrying your Qiankun pouch for most actions.) ")
        Util.updateframe(player)
        Util.runact(player, qk_pouch, input(""))

    @staticmethod
    def updateframe(player):
        # random event chance
        # debuff effects (bleeding, poison, disease, etc)
        enemies = Util.getenemies(player)
        if enemies != []:
            player.incombat = True
            for creature in enemies:
                print(creature.attack(player))
        else:
            player.incombat = False
        Util.growplants(player)
        print(Util.skilllvl(player))
        return

    @staticmethod
    def growplants(player):
        for field in player.plantedfields.keys():
            player.plantedfields[field][1] -= 1
            if player.plantedfields[field][1] == 0:
                plant = player.plantedfields[field][0]
                field.contents[plant.itemname] = plant.harvestamnt
                plant.amount[field] = plant.harvestamnt
                field.itemdesc -= f' There are {plant.itemname} seeds growing in this field.'


    @staticmethod
    def checkdate(player):
        msg = ""
        day = player.days%365
        if day == 0:
            player.age += 1
            msg = 'Happy birthday! The world of RMQM thanks you sincerely for your loyal devotion.'
        return msg

    @staticmethod
    def skilllvl(player):
        msg = ""
        for skill in player.skills.keys():
            lvlup = False
            currentlvl = player.skills[skill][0]
            exp = player.skills[skill][1]
            if currentlvl != 10:
                for i in range(currentlvl, 10):
                    match i:
                        case 0:
                            if exp >= 100:
                                lvlup = True
                        case 1:
                            if exp >= 250:
                                lvlup = True
                        case 2:
                            if exp >= 500:
                                lvlup = True
                        case 3:
                            if exp >= 750:
                                lvlup = True
                        case 4:
                            if exp >= 1000:
                                lvlup = True
                        case 5:
                            if exp >= 1500:
                                lvlup = True
                        case 6:
                            if exp >= 2000:
                                lvlup = True
                        case 7:
                            if exp >= 2500:
                                lvlup = True
                        case 8:
                            if exp >= 3000:
                                lvlup = True
                        case 9:
                            if exp >= 4000:
                                lvlup = True
                    i += 1
            if lvlup == True:
                currentlvl += 1
                msg += f'\nYour {skill} skill leveled up! It is now at level {currentlvl}.'
        return msg

    @staticmethod
    def getenemies(player):
        enemies = []
        for creature in player.playloc.npcs.values():
            if creature.isHostile == True:
                enemies.append(creature)
        return enemies

    @staticmethod
    def rename(player, thing):
        if thing in player.weapons:
            newname = input(f'What do you want to rename {thing} to?')
            player.weapons[thing].itemname = newname
            player.weapons[newname] = player.weapons.pop(thing)
            player.onplayer[newname] = player.onplayer.pop(thing)
            return f'{thing.capitalize()} has been renamed to {newname}'
        elif thing in player.instruments:
            newname = input(f'What do you want to rename {thing} to?')
            player.instruments[thing].itemname = newname
            player.instruments[newname] = player.instruments.pop(thing)
            player.onplayer[newname] = player.onplayer.pop(thing)
            return f'{thing.capitalize()} has been renamed to {newname}'
        else:
            return "What do you want to rename?"

    @staticmethod
    def changeinfo(player, info):
        match info:
            case "sect":
                return "To change your sect, you must apply for a sect change to your desired sect's leader."
            case "surname":
                player.surname = input("What would you like to change your surname to? ")
                return f'Your surname is now {player.surname}.'
            case "birth name":
                player.birthname = input("What would you like to change your birth name to? ")
                return f'Your birth name is now {player.birthname}.'
            case "courtesy name":
                court = input("You may only change one character of your courtesy name at a time. Would you like to change your 1. first or 2. second character? ")
                match court:
                    case "1":
                        player.courtname1 = input("What would you like to change the first character of your courtesy name to? ")
                        player.courtname = player.courtname1.capitalize() + player.courtname2.lower()
                        return f'Your courtesy name is now {player.courtname}.'
                    case "2":
                        player.courtname2 = input("What would you like to change the second character of your courtesy name to? ")
                        player.courtname = player.courtname1.capitalize() + player.courtname2.lower()
                        return f'Your courtesy name is now {player.courtname}.'
                    case other:
                        print("That is not a valid number.")
                        Util.changeinfo(player, "courtesy name")
            case "pronouns":
                player.setprn(input("What would you like to change your pronouns to? "))
                return f'Your pronouns are now {player.pronouns["subjprn"]}/{player.pronouns["objpronoun"]}.'
            case "honorific":
                player.sethonorific(input("What would you like to change your honorifics to? (1. Meimei and jiejie 2. Didi and gege) "))
                return f'Your honorifics are now {player.jieorge}{player.jieorge} and {player.meiordi}{player.meiordi}.'
            case other:
                return "You cannot change that."

    @staticmethod
    def getitemfromfree(player, itemname):
        container = ""
        item = ""
        try:
            if itemname in player.inv.contents:
                container = player.inv
                item = player.inv.contents[itemname]
            elif itemname == player.inv.itemname:
                item = player.inv
        except:
            pass
        if itemname in player.playloc.items or itemname in player.playloc.hidden_items:
            container = player.playloc
            item = player.playloc.getitem(itemname)
        elif itemname in player.onplayer:
            container = player
            item = player.onplayer[itemname]
        return [container, item]
    @staticmethod
    def examine(player, itemname, containername):
        if containername != None:
            container = Util.getitemfromunknown(player, None, containername)[0]
            item = Util.getitemfromunknown(player, container, itemname)[0]
        else:
            if itemname == "room":
                return player.playloc.getdescription(player)
            if itemname == "self" or itemname == "me":
                try:
                    return player.getdescription()
                except:
                    return player.getdescription()
            try:
                if itemname == player.inv.itemname:
                    return player.inv.getcontainerdescription(player)
            except:
                pass
            try:
                item = player.playloc.items[itemname]
                container = player.playloc
            except:
                try:
                    item = player.playloc.hidden_items[itemname]
                    container = player.playloc
                except:
                    try:
                        item = player.inv.contents[itemname]
                        container = player
                    except:
                        try:
                            item = player.onplayer[itemname]
                            container = player
                        except:
                            return "What are you trying to examine?"
        return item.examineitem(player, container)

    @staticmethod
    def take(player, qk_pouch, itemname, containername):
        item = None
        container = None
        if containername != None:
            list = Util.getitemfromunknown(player, None, containername)
            container = list[0]
        else:
            if itemname in player.playloc.items or itemname in player.playloc.hidden_items:
                container = player.playloc
                item = player.playloc.getitem(itemname)
            else:
                return "What are you trying to take?"
        return player.takeitem(qk_pouch, item, container)

    @staticmethod
    def getitemfromunknown(player, container, itemname):
        item = None
        for thing in player.playloc.items.values():
            if thing.itemname == itemname:
                return [thing, player.playloc]
            elif thing.isContainer == True:
                arr = Util.getitemfromcontainer(player, thing, itemname)
                if arr != [None, None]:
                    item = arr[0]
                    container = arr[1]
        for thing in player.playloc.hidden_items.values():
            if thing.itemname == itemname:
                return [thing, player.playloc]
            elif thing.isContainer == True:
                arr = Util.getitemfromcontainer(player, thing, itemname)
                if arr != [None, None]:
                    item = arr[0]
                    container = arr[1]
        for thing in player.onplayer.values():
            if thing.itemname == itemname:
                return [thing, player]
        try:
            for thing in player.inv.contents.values():
                if thing.itemname == itemname:
                    return [thing, player.inv]
                elif thing.isContainer == True:
                    arr = Util.getitemfromcontainer(player, thing, itemname)
                    if arr != [None, None]:
                        item = arr[0]
                        container = arr[1]
        except:
            pass
        return [item, container]

    @staticmethod
    def getitemfromcontainer(player, container, itemname):
        for thing in container.contents.values():
            if thing.itemname == itemname:
                item = thing
                return [item, container]
            elif thing.isContainer == True:
                Util.getitemfromcontainer(player, thing, itemname)
        return [None, None]

    @staticmethod
    def numberofitems(player, item, location):
        description = " "
        try:
            if location == player.inv:
                description += f'You have {str(item.amount[player.inv])} {item.itemname}'
                if item.amount[player.inv] != 1:
                    description += "s"
        except:
            pass
        if location == player:
            description += f'You are wearing this {item.itemname}'
        else:
            description += "There "
            if item.amount[location] == 1:
                description += f'is '
            else:
                description += f'are '
            description += f'{str(item.amount[location])} {item.itemname}'
            if item.amount[location] != 1:
                description += "s"
            if location == player.playloc:
                description += " in the room"
            elif location == None:
                return None
            else:
                description += f' {location.inoron} this {location.itemname}'
        description += f'.'
        return description

    @staticmethod
    def getamount(container, item, action):
        amount = input(f'How many {item.itemname}s do you want to {action}?')
        match action:
            case "take":
                if amount <= item.amount[container]:
                    return amount
                else:
                    print(f'There are less than {amount} {item.itemname}s here.')
                    Util.getamount(container, item, action)
            case "eat":
                if amount <= item.amount[container]:
                    return amount
                else:
                    print(f'You have less than {amount} {item.pluralitemname}.')
                    Util.getamount(container, item, action)
            case "put":
                if amount <= item.amount[container]:
                    return amount
                else:
                    print(f'There are less than {amount} {item.itemname}s here.')
                    Util.getamount(container, item, action)

    @staticmethod
    def chance(stat):
        chance = randint(1, 100)
        if chance <= stat:
            return True
        else:
            return False
