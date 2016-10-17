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
import re


class ShoppingListApp(App):
    def build(self):
        self.title = "Shopping List"
        self.root = Builder.load_file('app.kv')
        self.items = ItemList()
        items_as_list = load_items()
        self.items.add_item_lists(items_as_list)
        self.handle_listRequired()
        return self.root

    def handle_listRequired(self):
        """
        Search for and create the buttons for the required items
        :return:
        """

        item_required = "r"

        # Clears all the widgets that were already in the items_list_display area before creating the new widgets
        self.root.ids.items_list_display.clear_widgets()

        # get_total_price gets the total price of all the required items only and displays them in the status bar
        total_price = self.items.get_total_price()
        self.root.ids.status_bar.text = "Click an item to mark it as completed"

        # create the widgets for the required items
        for item in self.items.items:
            if item.status == item_required:
                self.temp_button = Button(text=item.name)
                self.temp_button.bind(on_release=self.click_required_item)
                self.root.ids.items_list_display.add_widget(self.temp_button)

        self.root.ids.details_bar.text = ("{:20} $ {:6.2f}".format("The total cost is:", total_price))

    def click_required_item(self, instance):
        """
        Change the item that was clicked to completed, and remove its widget required widget
        :param instance:
        """
        name = instance.text
        item = self.items.get_item_by_name(name)
        item.mark_item_as_complete()
        self.root.ids.status_bar.text = "Changed {} to completed".format(name)
        self.root.ids.items_list_display.remove_widget(instance)

    def handle_listCompleted(self):
        """
        Search for and create the buttons for the completed items
        """
        item_required = "c"

        # Clears all the widgets that were already in the items_list_display area before creating the new widgets
        self.root.ids.items_list_display.clear_widgets()

        self.root.ids.status_bar.text = "Click an item to mark it as completed"

        # Create all the widgets for all of the completed items
        for item in self.items.items:
            if item.status == item_required:
                self.temp_button = Button(text=item.name)
                self.temp_button.bind(on_release=self.click_completed_item)
                self.root.ids.items_list_display.add_widget(self.temp_button)

        self.root.ids.details_bar.text = "Showing completed items"
        self.root.ids.status_bar.text = "Click an item to see its details"

    def click_completed_item(self, instance):
        name = instance.text
        item = self.items.get_item_by_name(name)
        self.root.ids.status_bar.text = "{}, ${}, priority {} (completed)".format(item.name, item.price, item.priority)

    def handle_addItem(self):
        """
        Adds a new item
        """
        name = self.root.ids.item_name.text
        price = self.root.ids.item_price.text
        priority = self.root.ids.item_priority.text
        status = "r"
        item = self.items.add_new_item(name, price, priority, status)
        self.root.ids.status_bar.text = "Added {} - ${} to your shopping list".format(name, price, priority)

        # Clear the input fields
        self.root.ids.item_name.text = ''
        self.root.ids.item_price.text = ''
        self.root.ids.item_priority.text = ''

    def handle_clear(self):
        """
        Clears all the input fields in the app
        """
        self.root.ids.item_name.text = ''
        self.root.ids.item_price.text = ''
        self.root.ids.item_priority.text = ''

ShoppingListApp().run()
