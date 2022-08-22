from util import Util

class NPC():
    def __init__(self, name):
        self.name = name
        
class Creature(NPC):
    def __init__(self, name, drops):
        super().__init__(name)
        self.drops = drops

class Character(NPC):
    def __init__(self, name):
        super().__init__(name)