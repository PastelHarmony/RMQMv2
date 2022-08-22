from util import Util

class NPC():
    def __init__(self, name):
        self.name = name
        
class Creature(NPC):
    def __init__(self, name, drops, killxp, isPassive, isHostile, stats, afflictions, special):
        super().__init__(name)
        self.drops = drops
        self.killxp = killxp
        self.isPassive = isPassive
        self.isHostile = isHostile
        self.stats = stats
        self.afflictions = afflictions
    def attack(self, player):
        msg = ""
        if "frozen" in self.afflictions:
            return f'The {self.name} is frozen.'
        for debuff in self.afflictions:
            match debuff:
                case "bleeding":
                    self.stats["health"] -= 1
                    msg += f'The {self.name} is {debuff}. It took 1 hit of damage. It has {self.stats["health"]} hit points left.'
                case "burning":
                    dmg = 10-self.stats["fire resistance"]
                    self.stats["health"] -= dmg
                    if dmg < 0: dmg = 0
                    if dmg == 1:
                        msg += f'The {self.name} is {debuff}. It took 1 hit of damage. It has {self.stats["health"]} hit points left.'
                    else:
                        msg += f'The {self.name} is {debuff}. It took {dmg} hits of damage. It has {self.stats["health"]} hit points left.'
            if self.stats["health"] <= 0: player.kill(self)
        # chance to dodge = player.stats["dexterity"]/500
        # if player dodge: return f'You dodged the {self.name}.'
        physdmg = self.stats["physical damage"] - player.stats["physical defense"]
        if physdmg < 0: physdmg = 0
        magicdmg = self.stats["spiritual damage"] - player.stats["spiritual defense"]
        if magicdmg < 0: magicdmg = 0
        dmg = physdmg + magicdmg
        player.stats["health"] -= dmg
        msg += f' The {self.name} attacked you and dealt {dmg} damage.'
        if player.stats["health"] <= 0: player.stats["health"] = 0
        msg += f' You have {player.stats["health"]} hit points left.'

class Character(NPC):
    def __init__(self, name):
        super().__init__(name)