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
        apple = Item("apple", "A red apple.", "food", {}, True, True, False, False, None, None, None, {})
        pear = Item("pear", "A yellow pear.", "food", {apple:"special"}, True, True, False, False, None, None, None, {})
        apple.uses[pear] = "special"
        fish = Item("fish", "A blue fish.", "food", {}, True, True, False, False, None, None, None, {})
        robe = Item("robe", "A white fish.", "robe", {}, True, True, False, False, None, None, None, {self.player:1})
        self.player.onplayer[robe.itemname] = robe
        pouch = Item("pouch", "A purple pouch.", "container", {}, True, True, True, False, {apple.itemname:apple, pear.itemname:pear, fish.itemname:fish}, False, "in", {})
        chest = Item("chest", "A wooden chest.", "container", {}, True, False, True, False,
                     {}, False, "in", {})
        start_room = Room("Laolu Inn", "Your Room", "Golden sunlight filters softly through the windows.",
                          "Silver moonlight gently brushes along the walls.",
                          "The pattering of the rain echoes loudly through the dim room.",
                          "Snow twirls outside the window, blowing wildly in the wind.",
                          "The room is fairly small, made of long planks of old cedar wood. There is a bed in the far left corner and a desk in the far right. At your sides are two large shelves. A small window lies to your north. To your south is the door to the hallway.",
                          {pouch.itemname:pouch, apple.itemname:apple}, {}, {})
        ll_hall_1 = Room("Laolu Inn", "Hall", "Sunshine bathes the hall in bright rays.",
                            "The hall is dark except for twinkling speckles of starlight.", "", "",
                            "It is slightly narrow, and the walls are worn with old stains and scuffs. To the west is a wide window. Another room lies down the hall to your east. Your room is to your north. There are uneven stairs leading down to the first floor.",
                            {chest.itemname:chest}, {}, {})
        chest.amount[ll_hall_1] = 1
        ll_hall_1.connects["north"] = start_room
        start_room.connects["south"] = ll_hall_1
        self.player.playloc = start_room
        apple.amount[pouch] = 1
        apple.amount[start_room] = 1
        pear.amount[pouch] = 1
        fish.amount[pouch] = 1
        pouch.amount[start_room] = 1
        self.player.hasPouch = True
        Util.runact(self.player, pouch, "examine room", time)
        Util.runact(self.player, pouch, "examine apple", time)
        Util.runact(self.player, pouch, "take apple", time)
        Util.runact(self.player, pouch, "examine apple", time)
        Util.runact(self.player, pouch, "examine pouch", time)
        Util.runact(self.player, pouch, "take pouch", time)
        Util.runact(self.player, pouch, "examine pouch", time)
        Util.runact(self.player, pouch, "examine room", time)
        Util.runact(self.player, pouch, "use apple and pear", time)
        Util.runact(self.player, pouch, "go south", time)
        Util.runact(self.player, pouch, "eat pear", time)
        Util.runact(self.player, pouch, "put apple down", time)
        Util.runact(self.player, pouch, "examine room", time)
        Util.runact(self.player, pouch, "put fish in chest", time)
        Util.runact(self.player, pouch, "examine pouch", time)
        Util.runact(self.player, pouch, "examine chest", time)
        Util.runact(self.player, pouch, "put apple down", time)
        Util.runact(self.player, pouch, "examine pouch", time)
        Util.runact(self.player, pouch, "examine room", time)
        Util.runact(self.player, pouch, "push apple", time)
        Util.runact(self.player, pouch, "push chest", time)
