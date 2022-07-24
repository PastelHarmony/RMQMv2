class Item:
 def __init__(self, itemname, type, isContainer, contents):
     self.itemname = itemname
     self.isContainer = isContainer
     self.contents = contents
     self.type = type