# create your ItemList class here

from item import Item

class ItemList:
    def __init__(self, name="", price=0, priority=1):
        self.items = []
        self.items_as_lists = []
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


    def get_item_as_lists(self, items_as_lists):
        """
        Get Items as lists
        """

        for item in self.items:
            items_as_lists.append([item.name, item.price, item.priority])
        return items_as_lists

    def get_item_by_name(self, name):
        """
        Gets an item by its name
        """
        for item in self.items:
            if item.name == name:
                return item

    def add_new_item(self, name, price, priority, status):
        """
        Adds a single item object to the items list attributes
        """
        new_item = [name, price, priority, status]
        self.items_as_lists.append(new_item)
        self.add_item_lists(self.items_as_lists)


    def get_total_price(self):
        """
        Gets the total price of all the items
        """
        total_price = 0.0
        item_required = "r"
        for item in self.items:
            if item.status == item_required:
                total_price += float(item.price)
        return total_price






