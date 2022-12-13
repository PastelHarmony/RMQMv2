from util import Util
from dialogue import Dialogue
from dialogue import QuestConditions
from npc import NPC
from npc import Creature
from npc import Character

class Room:
 def __init__(self, loc, subloc, daydesc, nightdesc, raindesc, snowdesc, gendesc, items, hiddenitems, npcs, hiddennpcs, quests, connects):
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
     self.quests = quests
     self.connects = connects
 def getdescription(self, player):
     description = f'{self.loc} > {self.subloc} \n\n {self.getweatherdesc(player)} {self.gendesc}'
     if len(self.items) != 0:
         description += f'\nIn this room, you can see{Util.getlistdescription(list(self.items.values()), self)}'
         description += "."
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
 def getweatherdesc(self, player):
     if player.time == "day":
         match player.weather:
             case "clear":
                 return self.daydesc
             case "rain":
                 return self.raindesc
             case "snow":
                 return self.snowdesc
             case other:
                 return "Time bug"
     elif player.time == "night":
         match player.weather:
             case "clear":
                 return self.nightdesc
             case "rain":
                 return self.raindesc
             case "snow":
                 return self.snowdesc
             case other:
                 return "Time bug"
 def getitem(self, ex):
     if ex in self.items:
         item = self.items[ex]
     elif ex in self.hidden_items:
         item = self.hidden_items[ex]
     else:
         return None
     return item