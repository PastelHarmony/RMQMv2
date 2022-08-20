class Util():
    @staticmethod
    def getlistdescription(listofitems):
        list = ""
        for i in range(len(listofitems)):
            word = listofitems[i]
            if i != 0:
                list += ","
            if i == len(listofitems)-1:
                list += " and"
            if word[0].lower() == "a" or word[0].lower() == "e" or word[0].lower() == "i" or word[0].lower() == "o" or word[0].lower() == "u":
                list += f' an {word}'
            else:
                list += f' a {word}'
        return list

    @staticmethod
    def runact(player, playloc, qk_pouch, action, time):
        if "examine" == action[:7]:
            itemname = action[8:]
            if " in " in action:
                arr = itemname.split(" in ")
                itemname = arr[0]
                containername = arr[1]
            else:
                containername = None
            print(Util.examine(player, playloc, qk_pouch, itemname, containername, time))
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
            print(Util.useitem(a, b))
        elif "take" == action[:4]:
            itemname = action[5:]
            if " from " in itemname:
                arr = itemname.split(" from ")
                itemname = arr[0]
                containername = arr[1]
            else:
                containername = None
            print(Util.take(player, playloc, qk_pouch, itemname, containername))
        else:
            print("What are you trying to do?")
        Util.runact(player, playloc, qk_pouch, input(""), time)

    @staticmethod
    def examine(player, playloc, qk_pouch, itemname, containername, time):
        if containername != None:
            container = Util.getitemfromcontainer(player, playloc, None, containername)[0]
            item = Util.getitemfromcontainer(player, playloc, container, itemname)[0]
        else:
            if itemname == "room":
                return playloc.getdescription(time)
            if itemname == "self" or itemname == "me":
                return player.getdescription(qk_pouch)
            if itemname in playloc.items or itemname in playloc.hidden_items:
                container = playloc
                item = playloc.getitem(itemname)
            elif itemname in qk_pouch.contents:
                container = qk_pouch
                item = qk_pouch.contents[itemname]
            elif itemname in player.onplayer:
                container = player
                item = player.onplayer[itemname]
            else:
                return "What are you trying to examine?"
        return item.examineitem(player, playloc, qk_pouch, container)

    @staticmethod
    def take(player, playloc, qk_pouch, itemname, containername):
        item = None
        container = None
        if containername != None:
            list = Util.getitemfromcontainer(player, playloc, None, containername)
            container = list[0]
        else:
            if itemname in playloc.items or itemname in playloc.hidden_items:
                container = playloc
                item = playloc.getitem(itemname)
            elif itemname in qk_pouch.contents or itemname in player.onplayer:
                return "You already have that item!"
            else:
                return "What are you trying to examine?"
        return player.takeitem(playloc, qk_pouch, item, container)

    @staticmethod
    def getitemfromcontainer(player, playloc, container, itemname):
        item = None
        if container is not None:
            for thing in container.contents.values():
                if thing.itemname == itemname:
                    item = thing
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, playloc, thing, itemname)
        else:
            for thing in playloc.items.values():
                if thing.itemname == itemname:
                    item = thing
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, playloc, thing, itemname)
                return [item, container]
            for thing in playloc.hidden_items.values():
                if thing.itemname == itemname:
                    item = thing
                elif thing.type == "container":
                    Util.getitemfromcontainer(player, playloc, thing, itemname)
                return [item, container]
        return [item, container]

    @staticmethod
    def numberofitems(player, playloc, qk_pouch, item, location):
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
            if location == playloc:
                description += " in the room"
            elif location == None:
                return None
            else:
                description += f' {location.inoron} this {location.itemname}'
        description += f'.'
        return description

    @staticmethod
    def useitem(itema, itemb):
        try:
            reaction = itema.uses[itemb]
        except:
            return "Those items don't do anything together."
        if reaction == "special":
            return itema.use(itemb)
        else:
            return reaction
