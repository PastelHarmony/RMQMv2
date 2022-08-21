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
            itema = Util.getitem(player, qk_pouch, a)[1]
            itemb = Util.getitem(player, qk_pouch, b)[1]
            print(Util.useitem(player, itema, itemb))
        elif "go" == action[:2]:
            arr = player.go(time, action[3:])
            print(arr[0])
            player.playloc = arr[1]
        elif "inv" == action:
            print(Util.examine(player, qk_pouch, "self", None, time))
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
                arr = action[4:].split(" in ")
                itemname = arr[0]
                containername = arr[1]
                Util.take(player, qk_pouch, itemname, containername)
            except:
                try:
                    item = qk_pouch.contents[itemname]
                except:
                    item = player.playloc.items[itemname]
            item = qk_pouch.contents[itemname]
            try:
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
        else:
            print("What are you trying to do?")
        # Util.runact(player, qk_pouch, input(""), time)
        return

    @staticmethod
    def getitem(player, qk_pouch, itemname):
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
        return [container, item]

    @staticmethod
    def examine(player, qk_pouch, itemname, containername, time):
        if containername != None:
            container = Util.getitemfromcontainer(player, None, containername)[0]
            item = Util.getitemfromcontainer(player, container, itemname)[0]
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
            list = Util.getitemfromcontainer(player, None, containername)
            container = list[0]
        else:
            if itemname in player.playloc.items or itemname in player.playloc.hidden_items:
                container = player.playloc
                item = player.playloc.getitem(itemname)
            elif itemname in qk_pouch.contents or itemname in player.onplayer:
                return "You already have that item!"
            else:
                return "What are you trying to take?"
        return player.takeitem(qk_pouch, item, container)

    @staticmethod
    def getitemfromcontainer(player, container, itemname):
        item = None
        if container is not None:
            for thing in container.contents.values():
                if thing.itemname == itemname:
                    item = thing
                    break
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, thing, itemname)
        else:
            for thing in player.playloc.items.values():
                if thing.itemname == itemname:
                    item = thing
                    break
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, thing, itemname)
                return [item, container]
            for thing in player.playloc.hidden_items.values():
                if thing.itemname == itemname:
                    item = thing
                    break
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, thing, itemname)
                return [item, container]
        return [item, container]

    @staticmethod
    def numberofitems(player, qk_pouch, item, location):
        description = " "
        if location == player:
            description += f'You have {str(item.amount[qk_pouch])} {item.itemname}'
            if item.amount[qk_pouch] != 1:
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

    @staticmethod
    def useitem(player, itema, itemb):
        if isinstance(itema, str):
            return "You don't have that item."
        try:
            reaction = itema.uses[itemb]
        except:
            return "Those items don't do anything together."
        if reaction == "special":
            return itema.use(itemb)
        else:
            return reaction
