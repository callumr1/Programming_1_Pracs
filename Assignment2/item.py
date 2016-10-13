# create your Item class here

class Item:
    def __init__(self, item_name = "", item_price = 0, item_importance = 1):
        self.item_name = item_name
        self.item_price = item_price
        self.item_importance = item_importance

    def __str__(self):
        return "{}, ${}, priority {} (completed)".format(self.item_name, self.item_price, self.item_importance)

    def mark_completed(self):

