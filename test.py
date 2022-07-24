from unittest import TestCase

from player import Player

from item import Item

from room import Room

from util import Util

class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player()

class TestItem(TestPlayer):
    def test_examine(self):
        brick = Item("brick", "A red brick", "misc", False, None, None, None)
        apple = Item("apple", "A red apple", "food", False, None, None, None)
        pear = Item("pear", "A yellow pear", "food", False, None, None, None)
        fish = Item("fish", "A blue fish", "food", False, None, None, None)
        pouch = Item("pouch", "A purple pouch.", "container", True, {apple.itemname:apple, pear.itemname:pear, fish.itemname:fish}, False, "in")
        start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.",
                          "Silver moonlight gently brushes along the walls.",
                          "The pattering of the rain echoes loudly through the dim room.",
                          "Snow twirls outside the window, blowing wildly in the wind.",
                          "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.",
                          {pouch.itemname:pouch}, {}, {})
        # print(Util.examine(self.player, start_room, "pouch"))
        print(Util.getlistdescription(["apple", "pear", "fish"]))