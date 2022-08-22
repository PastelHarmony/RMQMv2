from util import Util
from npc import NPC
from npc import Creature
from npc import Character

class Room:
 def __init__(self, loc, subloc, daydesc, nightdesc, raindesc, snowdesc, gendesc, items, hiddenitems, npcs, hiddennpcs):
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
     self.hidden_npcs = hiddennpcs
     self.connects = {}
 def getdescription(self, time):
     description = f'{self.loc} > {self.subloc} \n\n {self.get_timedesc(time)} {self.gendesc}'
     if len(self.items) != 0:
         description += f'\nIn this room, you can see{Util.getlistdescription(list(self.items.values()), self)}'
     if self.npcs != {}:
         description += "\nIn this room "
         creatures = []
         people = []
         for npc in self.npcs.values():
             if isinstance(npc, Character):
                people.append(f'{npc.name}')
             else:
                 creatures.append(npc.name)
         if creatures != []:
             description += f'is{Util.getlistdescription(creatures, self)}'
             if people!= []:
                 description += f'.{Util.basiclistdescription(people)} are also here'
         elif people != []:
             description += f'are{Util.basiclistdescription(people)}'
         description += "."
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