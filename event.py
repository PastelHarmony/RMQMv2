from util import Util

class Event():
    def __init__(self, name, conditions):
        self.eventname = name
        self.eventconditions = conditions

class Story(Event):
    def __int__(self, name, conditions):
        super().__init__(name, conditions)

class Quest(Event):
    def __int__(self, name, conditions, currentstep, stepamnt, overalldesc, stepname, stepdesc, completionreq, rewards):
        super().__init__(name, conditions)
        self.qcurrentstep = currentstep
        self.qstepamnt = stepamnt
        self.qoveralldesc = overalldesc
        self.qstepname = stepname
        self.qstepdesc = stepdesc
        self.qcompreq = completionreq # requirements for completion
        self.qrewards = rewards
        self.qisActive = False
        self.qisFinished = False
    def startquest(quest):
        quest.qcurrentstep = 1
        msg = f'You unlocked a new quest.' \
               f'{quest.eventname}' \
               f'{quest.qoveralldesc}' \
               f'Part {quest.qcurrentstep} - {quest.qstepname[quest.qcurrentstep]}' \
               f'{quest.qstepdesc[quest.qcurrentstep]}'
        for requirement in quest.qcompreq[quest.qcurrentstep]:
            msg += f'_ {requirement}'
        return
    def updatequest(self):
        msg = f'You completed \'{self.qstepname}\', step {self.qcurrentstep} out of {self.qstepamnt} in \'{self.qstepname}\''
        self.qcurrentstep += 1
        if self.qcurrentstep == self.qstepamnt:
            self.completequest()
        else:
            msg += f'Part {self.qcurrentstep} - {self.qstepname[self.qcurrentstep]}' \
               f'{self.qstepdesc[self.qcurrentstep]}'
        for requirement in self.qcompreq[self.qcurrentstep]:
            msg += f'_ {requirement}'
        return
    def completequest(self):
        self.qisFinished = True
        msg = f'You completed \'{self.qstepname}\'.'
        # give rewards
        return
    def questdesc(self):
        return

class Random(Event):
    def __int__(self, name, conditions):
        super().__init__(name, conditions)