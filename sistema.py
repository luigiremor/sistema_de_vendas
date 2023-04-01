
from manager import Manager
from cart import Cart
from cashier import Cashier
from storage import Storage


class Sistema:

    def __init__(self):
        self.storage: Storage = None
        self.cart: Cart = None
        self.user: Manager or Cashier = None

    def add_cart(self, cart):
        self.cart = cart

    def add_storage(self, storage):
        self.storage = storage

    def add_user(self, user):
        self.user = user

    def consult_storage_product(self, name):
        return self.storage.search_product(name)
    
    def insert_storage_product(self, product):
        if self.user.is_admin:
            self.storage.add_product(product)

    def remove_storage_product(self, product):
        if self.user.is_admin:
            self.storage.remove_product(product)

    def add_product_to_cart(self, product):
        self.storage.remove_product(product)
        self.cart.add_item(product)

    def remove_product_from_cart(self, product):
        self.cart.remove_item(product)
        self.storage.add_product(product)

    def total_cart(self):
        return self.cart.total()
    

