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
        time = "day"
        brick = Item("brick", "A red brick.", "misc", {}, True, False, False, None, None, None, {})
        apple = Item("apple", "A red apple.", "food", {}, True, False, False, None, None, None, {})
        pear = Item("pear", "A yellow pear.", "food", {apple:"special"}, True, False, False, None, None, None, {})
        apple.uses[pear] = "special"
        fish = Item("fish", "A blue fish.", "food", {}, True, False, False, None, None, None, {})
        pouch = Item("pouch", "A purple pouch.", "container", {}, True, True, False, {apple.itemname:apple, pear.itemname:pear, fish.itemname:fish}, False, "in", {})
        start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.",
                          "Silver moonlight gently brushes along the walls.",
                          "The pattering of the rain echoes loudly through the dim room.",
                          "Snow twirls outside the window, blowing wildly in the wind.",
                          "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.",
                          {pouch.itemname:pouch, apple.itemname:apple}, {}, {})
        apple.amount[pouch] = 1
        apple.amount[start_room] = 1
        pear.amount[pouch] = 1
        fish.amount[pouch] = 1
        pouch.amount[start_room] = 1
        self.player.hasPouch = True
        Util.runact(self.player, start_room, pouch, "examine room", time)
        Util.runact(self.player, start_room, pouch, "examine apple", time)
        Util.runact(self.player, start_room, pouch, "take apple", time)
        Util.runact(self.player, start_room, pouch, "examine apple in pouch", time)
        Util.runact(self.player, start_room, pouch, "examine pouch", time)
        Util.runact(self.player, start_room, pouch, "take pouch", time)
        Util.runact(self.player, start_room, pouch, "examine room", time)
        Util.runact(self.player, start_room, pouch, "use apple and pear", time)
