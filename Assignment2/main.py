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
        self.items_as_list = load_items()
        self.items.add_item_lists(self.items_as_list)
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
                # Determines the color of the button depending on the items priority
                if item.priority == "1":
                    color = (255, 0, 0, 0.6)
                elif item.priority == "2":
                    color = (0, 255, 0, 0.6)
                else:
                    color = (0, 0, 255, 0.6)

                self.items.sort_items_by_priority(item.priority)
                self.temp_button = Button(text=item.name, background_color=color)
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
        # Changes the item that was clicked from required to completed
        name = instance.text
        item = self.items.get_item_by_name(name)
        self.root.ids.status_bar.text = "{}, ${:.2f}, priority {} (completed)".format(item.name, float(item.price), item.priority)

    def handle_addItem(self):
        """
        Adds a new item
        """

        if self.root.ids.item_name.text == "" or self.root.ids.item_price.text == "" or self.root.ids.item_priority.text == "":
            self.root.ids.status_bar.text = "Please fill all input fields before adding an item"
            # Clear the input fields
            self.handle_clear()
        else:
            if self.root.ids.item_priority.text == "1" or self.root.ids.item_priority.text == "2" or self.root.ids.item_priority.text == "3":
                try:
                    price = float(self.root.ids.item_price.text)
                    if re.match(r'^\d+$', self.root.ids.item_name.text):
                        self.root.ids.status_bar.text = "Item name must not be a number"
                        self.handle_clear()
                    else:
                        name = self.root.ids.item_name.text
                        price = float(self.root.ids.item_price.text)
                        priority = self.root.ids.item_priority.text
                        status = "r"
                        item = self.items.add_new_item(name, price, priority, status)
                        self.root.ids.status_bar.text = "Added {} - ${} to your shopping list".format(name, price, priority)
                        self.handle_clear()

                        # Refresh the item widgets once the new item is added
                        self.handle_listRequired()
                except ValueError:
                    self.root.ids.status_bar.text = "The price must be a float"
                    self.handle_clear()
            else:
                self.root.ids.status_bar.text = "The item priority can only be 1, 2 or 3"
                self.handle_clear()


    def handle_clear(self):
        """
        Clears all the input fields in the app
        """
        self.root.ids.item_name.text = ''
        self.root.ids.item_price.text = ''
        self.root.ids.item_priority.text = ''

ShoppingListApp().run()
