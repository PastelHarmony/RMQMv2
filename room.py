from util import Util

class Room:
 def __init__(self, loc, subloc, daydesc, nightdesc, raindesc, snowdesc, gendesc, items, hiddenitems, npcs):
     self.loc = loc
     self.subloc = subloc
     self.daydesc = daydesc
     self.nightdesc = nightdesc
     self.raindesc = raindesc
     self.snowdesc = snowdesc
     self.gendesc = gendesc
     self.items = items
     self.hidden_items = hiddenitems
     self.npcs = npcs
     self.connects = {}
 def getdescription(self, time):
     sep = ", a "
     description = self.loc + " > " + self.subloc + "\n\n" + self.get_timedesc(time) + " " + self.gendesc
     if len(self.items) != 0:
         description += "\nIn this room, you can see" + Util.getlistdescription(list(self.items.values()), self) + "."
     if self.npcs != {}:
         description += "\nThere is a" + sep.join(self.npcs)
     return description
 def get_timedesc(self, time):
     if time == "day":
         return self.daydesc
     elif time == "night":
         return self.nightdesc
     elif time == "rain":
         return self.raindesc
     elif time == "snow":
         return self.snowdesc
 def getitem(self, ex):
     if ex in self.items:
         item = self.items[ex]
     elif ex in self.hidden_items:
         item = self.hidden_items[ex]
     else:
         return None
     return item