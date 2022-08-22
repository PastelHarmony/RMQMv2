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
    def runact(player, qk_pouch, action, time):
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
            print(Util.examine(player, qk_pouch, itemname, containername, time))
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
            itema = Util.getitemfromfree(player, qk_pouch, a)[1]
            itemb = Util.getitemfromfree(player, qk_pouch, b)[1]
            print(player.useitem(itema, itemb))
        elif "go" == action[:2]:
            arr = player.go(time, action[3:])
            print(arr[0])
            player.playloc = arr[1]
        elif "inv" == action:
            description = Util.examine(player, qk_pouch, "self", None, time)
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
                        item = qk_pouch.contents[itemname]
                    except:
                        item = player.playloc.items[itemname]
                item = qk_pouch.contents[itemname]
                if item.type == "food":
                    print(player.eat(qk_pouch, item))
                else:
                    print("You can't eat that.")
            except:
                print("What are you trying to eat?")
        elif "put" == action[:3]:
            if "down" in action[4:]:
                arr = action[4:].split(" ")
                itemname = arr[0]
                containername = "down"
                print(player.put(qk_pouch, itemname, containername))
            else:
                try:
                    arr = action[4:].split(" in ")
                    itemname = arr[0]
                    containername = arr[1]
                    print(player.put(qk_pouch, itemname, containername))
                except:
                    try:
                        arr = action[4:].split(" on ")
                        itemname = arr[0]
                        containername = arr[1]
                        print(player.put(qk_pouch, itemname, containername))
                    except:
                        print("Where are you trying to put that?")
        elif "push" == action[:4]:
            item = Util.getitemfromunknown(player, None, action[5:])[0]
            print(player.push(item))
        elif "wear" == action[:4]:
            item = Util.getitemfromunknown(player, None, action[5:])[0]
            print(player.wear(qk_pouch, item))
        elif "undress" == action[:7]:
            item = player.onplayer[action[8:]]
            print(player.undress(qk_pouch, item))
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
                        print(player.attack(creature, weapon))
                    except:
                        try:
                            weapon = player.instruments[arr[1]]
                            print(player.attack(creature, weapon))
                        except:
                            print("What are you trying to attack the creature with?")
                except:
                    print("What are you trying to attack?")
            except:
                print(f'What are you trying to attack the creature with?')
        else:
            print("What are you trying to do?")
        Util.updateframe()
        Util.runact(player, qk_pouch, input(""), time)

    @staticmethod
    def updateframe():
        # random event chance
        # if hostile enemies, player.incombat = True
        # if player.incombat = True:
        #
        return

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
    def getitemfromfree(player, qk_pouch, itemname):
        container = ""
        item = ""
        if itemname in player.playloc.items or itemname in player.playloc.hidden_items:
            container = player.playloc
            item = player.playloc.getitem(itemname)
        elif itemname in qk_pouch.contents:
            container = qk_pouch
            item = qk_pouch.contents[itemname]
        elif itemname in player.onplayer:
            container = player
            item = player.onplayer[itemname]
        elif itemname == qk_pouch.itemname:
            item = qk_pouch
        return [container, item]
    @staticmethod
    def examine(player, qk_pouch, itemname, containername, time):
        if containername != None:
            container = Util.getitemfromunknown(player, None, containername)[0]
            item = Util.getitemfromunknown(player, container, itemname)[0]
        else:
            if itemname == "room":
                return player.playloc.getdescription(time)
            if itemname == "self" or itemname == "me":
                return player.getdescription(qk_pouch)
            if itemname == qk_pouch.itemname:
                return qk_pouch.getcontainerdescription(player)
            try:
                item = player.playloc.items[itemname]
                container = player.playloc
            except:
                try:
                    item = qk_pouch.contents[itemname]
                    container = player
                except:
                    try:
                        item = player.onplayer[itemname]
                        container = player
                    except:
                        return "What are you trying to examine?"
        return item.examineitem(player, qk_pouch, container)

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
                item = thing
                return [item, container]
            elif thing.isContainer == True:
                arr = Util.getitemfromcontainer(player, thing, itemname)
                if arr != [None, None]:
                    item = arr[0]
                    container = arr[1]
        for thing in player.playloc.hidden_items.values():
            if thing.itemname == itemname:
                item = thing
                return [item, container]
            elif thing.isContainer == True:
                arr = Util.getitemfromcontainer(player, thing, itemname)
                if arr != [None, None]:
                    item = arr[0]
                    container = arr[1]
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
    def numberofitems(player, qk_pouch, item, location):
        description = " "
        if location == qk_pouch:
            description += f'You have {str(item.amount[qk_pouch])} {item.itemname}'
            if item.amount[qk_pouch] != 1:
                description += "s"
        elif location == player:
            description += f'You have {str(item.amount[player])} {item.itemname}'
            if item.amount[player] != 1:
                description += "s"
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