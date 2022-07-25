from util import Util

class Item:
 def __init__(self, itemname, itemdesc, type, canTake, isRegenerative, isContainer, contents, isLocked, inoron, amount):
     self.itemname = itemname
     self.itemdesc = itemdesc
     self.canTake = True
     self.isRegenerative = False
     self.isContainer = isContainer
     self.contents = contents
     self.type = type
     self.isLocked = isLocked
     self.inoron = inoron
     self.amount = amount
 def examineitem(self, player, playloc, qk_pouch, location):
     description = self.getitemdescription(player)
     if self.type == "container":
         description = self.getcontainerdescription(player, playloc, qk_pouch)
     description += Util.numberofitems(player, playloc, qk_pouch, self, location)
     return description
 def getitemdescription(self, player):
     if self.itemname == "Qiankun pouch":
        description = "A small " + player.sectcolors + " bag made of thick silk. It is secured with a silver drawstring and embroidered with intricate " + player.sectsym + "s. It can hold an unlimited amount of objects."
     elif self.itemname == "calligraphy brush":
        description = f'A sleek calligraphy brush with a {player.sectsym}-engraved wooden handle and long, dark bristles.'
     elif self.itemname == "inkstone":
        description = f'A simple {player.sectcolors} porcelain inkstone with {player.sectsym} engravings.'
     elif self.itemname == "inkstick":
        description = f'A plain black inkstick carved into a {player.sectsym} at the end.'
     else:
        description = self.itemdesc
     return description
 def getcontainerdescription(self, player, playloc, qk_pouch):
     description = self.getitemdescription(player)
     if self.isLocked == False:
         if len(self.contents) != 0:
             sep = ", a "
             description += " " + self.inoron.capitalize() + " it is" + Util.getlistdescription(player, playloc, qk_pouch, list(self.contents.keys())) + "."
         else:
             description += " There is nothing " + self.inoron + " the " + self.itemname + "."
     else:
         description += f' You try to open the {self.itemname} but it\'s locked.'
     return description