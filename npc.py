from util import Util

class NPC():
    def __init__(self, type):
        self.type = type
        
class Creature(NPC):
    def __init__(self, type):
        super().__init__(type)

class Character(NPC):
    def __init__(self, type):
        super().__init__(type)