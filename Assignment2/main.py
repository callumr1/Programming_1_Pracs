""" Callum Robertson
    10/10/16
    Description
    Link """
# starting with importing from your first assignemnt, something like:

from shopping_list_2 import load_items, save_items
from kivy.app import App
from kivy.lang import Builder



class ShoppingListApp(App):
    items = []
    load_items(items)

    print(items)
    def build(self):
        self.title = "Shopping List"
        self.root = Builder.load_file('app.kv')
        return self.root

    def handle_listRequired(self):
        total_cost = 0.0
        self.root.ids.status_bar.text = "Click an item to mark it as completed"

        self.root.ids.details_bar.text = ("{:20} $ {:6.2f}".format("The total cost is:", total_cost))


    def handle_listCompleted(self):
        self.root.ids.details_bar.text = "Showing completed items"
        self.root.ids.status_bar.text = "Click an item to see its details"

    def handle_addItem(self):
        self.root.ids.status_bar.text = "Added {} - ${} to your shopping list"

    def handle_clear(self):
        self.root.ids.item_name.text = ''
        self.root.ids.item_price.text = ''
        self.root.ids.item_priority.text = ''

ShoppingListApp().run()