from unittest import TestCase

from player import Player

from item import Item

from room import Room

class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player()

class TestItem(TestCase):
    def setUp(self):
        brick = Item("brick", "A red brick", "misc", False, None, None, None)
        apple = Item("apple", "A red apple", "food", False, None, None, None)