# create your ItemList class here

from item import Item

class ItemList:
    def __init__(self, name=""):
        self.items = []
        self.name = name

    def add_item_lists(self, items_as_lists):
        """
        Add all items to items list
        :param items_as_lists:
        :return: none
        """

        for item_as_list in items_as_lists:
            i = Item(*item_as_list)
            self.items.append(i)


    def get_item_as_lists(self):
        """
        Get Items as lists
        """

        items_as_lists = []
        for item in self.items:
            items_as_lists.append([item.name, item.price, item.priority])
        return items_as_lists

    def get_item_by_name(self, name):
        """
        Gets an item by its name
        """
        for item in self.items:
            if self.name in item:
                return item

    def add_item(self):
        """
        Adds a single item object to the items list attributes
        """

    def get_total_price(self, price):
        """
        Gets the total price of all the items
        """
        total_cost = 0.0
        total_cost += float(price)



