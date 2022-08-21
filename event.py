from util import Util

class Event():
    def __init__(self, name):
        self.name = name

class Story(Event):
    def __int__(self, name):
        super().__init__(name)

class Quest(Event):
    def __int__(self, name):
        super().__init__(name)

class Random(Event):
    def __int__(self, name):
        super().__init__(name)