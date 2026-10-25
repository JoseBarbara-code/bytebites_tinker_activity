# Customer: Stores a customer's name and purchase history.
# FoodItem: Stores an item's name, price, category, and popularity rating.
# Menu: Stores the collection of food items.
# Order: Stores a customer and their selected items.

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []  # list of Order objects

    def add_purchase(self, order):
        self.purchase_history.append(order)


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []  # list of FoodItem objects

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        matching_items = []
        for item in self.items:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    def sort_by_popularity(self):
        # sorted() returns a new list, so self.items keeps its order
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  # list of FoodItem objects

    def add_item(self, item):
        self.items.append(item)

    def compute_total(self):
        total = 0
        for item in self.items:
            total = total + item.price
        return total
