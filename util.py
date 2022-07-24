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
        # word = listofitems[len(listofitems)-1]
        # if word[0].lower() == "a" or "e" or "i" or "o" or "u":
            # list += f' and an {word}'
        # else:
            # list += f' and a {word}'
        return list

    @staticmethod
    def runact(player, playloc, action):
        if "examine" == action[:7]:
            itemname = action[8:]
            print(Util.examine(player, playloc, itemname))
        else:
            print("What are you trying to do?")
        Util.runact(player, playloc, input(""))

    @staticmethod
    def examine(player, playloc, itemname):
        item = None
        if itemname in playloc.items or itemname in playloc.hidden_items:
            item = playloc.getitem(itemname)
        elif itemname in player.inv or itemname in player.onplayer:
            item = player.getitem(itemname)
        if item is None:
            return "What are you trying to examine?"
        else:
            return item.examineitem(player)
