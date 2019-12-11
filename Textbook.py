# Gavin Howard
# 11/20/19
# Textbook Class

from PersonClass import Person


class Textbook:
    def __init__(self, title, first, last, age, edition, isbn, publisher, year_pub, quantity_available, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.isbn = isbn
        self.publisher = publisher
        self.year_pub = year_pub
        self.quantity_available = quantity_available
        self.price = price

    def add_inventory(self, qty):
        self.quantity_available = self.quantity_available + qty

    def deduct_inventory(self, qty):
        if self.quantity_available >= qty:
            self.quantity_available = self.quantity_available - qty
            return 0
        else:
            return 1

    def reorder_warning(self):
        if self.quantity_available <= 5:
            return "Time to reorder"
        else:
            return "Inventory level is adequate"
