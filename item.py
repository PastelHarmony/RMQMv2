class Item:
 def __init__(self, itemname, itemdesc, type, isContainer, contents, isLocked, inoron):
     self.itemname = itemname
     self.itemdesc = itemdesc
     self.isContainer = isContainer
     self.contents = contents
     self.type = type
     self.isLocked = isLocked
     self.inoron = inoron
 def examineitem(self, player):
     description = self.getitemdescription(player)
     if self.type == "container":
         description = self.getcontainerdescription(player)
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
 def getcontainerdescription(self, player):
     description = self.getitemdescription(player)
     if self.isLocked == False:
         if len(self.contents) != 0:
             sep = ", a "
             description += " " + self.inoron.capitalize() + "side it is a " + sep.join(self.contents) + "."
         else:
             description += " There is nothing " + self.inoron + " the " + self.itemname + "."
     else:
         description += f' You try to open the {self.itemname} but it\'s locked.'
     return description