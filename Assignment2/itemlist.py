# create your ItemList class here

from item import Item

class ItemList:
    def __init__(self, items):
        self.items = items

    def addItem(item_name, item_price, item_priority):
        item = Item(item_name, item_price, item_priority)
        return item


