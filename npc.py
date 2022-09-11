from util import Util

class NPC():
    def __init__(self, name):
        self.name = name
        
class Creature(NPC):
    def __init__(self, name, drops, killxp, isPassive, isHostile, stats, afflictions, isLiquid):
        super().__init__(name)
        self.drops = drops
        self.killxp = killxp
        self.isPassive = isPassive
        self.isHostile = isHostile
        self.stats = stats
        self.afflictions = afflictions
        isLiquid = isLiquid
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
        if player.stats["health"] == 0: return player.die()
        return msg

class Character(NPC):
    def __init__(self, surname, birthname, courtname, npctitle, npcsect, npcnamelist, yournamelist, intlvls, relationship):
        super().__init__(f'{surname} {courtname}')
        self.npcsurname = surname
        self.npcbirthname = birthname
        self.npccourtname = courtname
        self.npctitle = npctitle
        self.npcsect = npcsect
        self.npcnamelist = npcnamelist # {-2: self.npctitle, -1: self.npctitle, 0: self.npctitle, 1: self.name,
                            # 2: self.npccourtname, 3: self.sectorcourt(player), 4: self.sectorcourt(player), 5: self.npcsurname + self.npcbirthname,
                            # 6: self.npcsurname + self.npcbirthname, 7: self.npcbirthnick, 8: self.npcbirthnick, 9: self.npczhiji,
                            # 10: self.npczhiji}
        self.yournamelist = yournamelist # {-2: player.courtname, -1: player.courtname, 0: player.courtname,
                             # 1: player.sectorcourt(self), 2: player.sectorcourt(self), 3: self.callsyoucourt,
                             # 4: self.callsyoucourt, 5: (player.surname + " " + player.birthname),
                             # 6: (player.surname + " " + player.birthname), 7: self.callsyoubirth, 8: self.callsyoubirth,
                             # 9: "A-" + player.birthname}
        self.npccalled = self.npcnamelist[0]
        self.callsyou = self.yournamelist[0]
        self.intpoints = 0
        self.intimacy = 0
        self.intlvls = intlvls
        self.relationship = relationship
    def getintimacy(self, amnt):
        pre = self.intimacy
        self.intpoints += amnt
        if self.intpoints <= self.intlvls[-2]:
            self.intimacy = -2
            self.npccalled = self.npcnamelist[-2]
            self.callsyou = self.yournamelist[-2]
        elif self.intpoints <= self.intlvls[-1]:
            self.intimacy = -1
            self.npccalled = self.npcnamelist[-1]
            self.callsyou = self.yournamelist[-1]
        for i in range(0, 10):
            if self.intpoints >= self.intlvls[i]:
                self.intimacy = i
                self.npccalled = self.npcnamelist[i]
                self.callsyou = self.yournamelist[i]
        if pre != self.intimacy:
            return f'{self.name} now considers you their {self.relationship[self.intimacy]}!'