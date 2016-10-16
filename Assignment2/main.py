""" Callum Robertson
    10/10/16
    Description
    Link """
# starting with importing from your first assignemnt, something like:

from shopping_list_2 import load_items, save_items
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from itemlist import ItemList
from item import Item



class ShoppingListApp(App):


    def build(self):
        self.title = "Shopping List"
        self.root = Builder.load_file('app.kv')
        self.items = ItemList()
        items_as_list = load_items()
        self.items.add_item_lists(items_as_list)
        return self.root

    def handle_listRequired(self):
        """
        Search for and create the buttons for the required items
        :return:
        """

        item_required = "r"

        total_cost = 0.0
        self.root.ids.status_bar.text = "Click an item to mark it as completed"
        for item in self.items.items:
            if item.status == item_required:
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.click_required_item)
                self.root.ids.items_list_display.add_widget(temp_button)

        self.root.ids.details_bar.text = ("{:20} $ {:6.2f}".format("The total cost is:", total_cost))

    def click_required_item(self, instance):
        name = instance.text
        ItemList(name)



    def handle_listCompleted(self):
        """
        Search for and create the buttons for the completed items
        :return:
        """
        item_required = "c"


        self.root.ids.status_bar.text = "Click an item to mark it as completed"
        for item in self.items.items:
            if item.status == item_required:
                temp_button = Button(text=item.name)
                temp_button.bind(on_release=self.click_required_item)
                self.root.ids.items_list_display.add_widget(temp_button)

        self.root.ids.details_bar.text = "Showing completed items"
        self.root.ids.status_bar.text = "Click an item to see its details"

    def handle_addItem(self):
        """
        Adds a new item
        """
        self.root.ids.status_bar.text = "Added {} - ${} to your shopping list"

    def handle_clear(self):
        """
        Clears all the input fields in the app
        """
        self.root.ids.item_name.text = ''
        self.root.ids.item_price.text = ''
        self.root.ids.item_priority.text = ''

ShoppingListApp().run()