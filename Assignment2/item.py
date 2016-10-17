# create your Item class here

class Item:
    def __init__(self, name="", price=0.0, priority=1, status='r'):
        self.name = name
        self.price = float(price)
        self.priority = priority
        self.status = status

    def __str__(self):
        return "{}, ${}, priority {} (completed)".format(self.name, self.price, self.priority)

    def mark_item_as_complete(self):
        """
        changes an item from required to complete
        :return:
        """
        self.status = "c"
