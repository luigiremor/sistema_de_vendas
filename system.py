
from manager import Manager
from cart import Cart
from cashier import Cashier
from storage import Storage


class System:

    def __init__(self):
        self.storage: Storage = None
        self.cart: Cart = None
        self.user: Manager or Cashier = None
        self.disconnecteds: list[Manager or Cashier] = []

    def add_cart(self, cart):
        self.cart = cart

    def add_storage(self, storage):
        self.storage = storage

    def add_user(self, user):
        self.user = user

    def login(self, username, password):
        if self.user is None:
            for user in self.disconnecteds:
                if user.authenticate(username, password):
                    self.user = user
                    self.disconnecteds.remove(user)
                    return True
            return False
        else:
            return self.user.authenticate(username, password)
    
    def logout(self):
        self.disconnecteds.append(self.user)
        self.user = None

    def consult_storage_product(self, name):
        return self.storage.search_product(name)
    
    def insert_storage_product(self, product, qtd=1):
        if self.user._is_admin:
            self.storage.add_product(product, qtd)

    def remove_storage_product(self, product, qtd=1):
        if self.user._is_admin:
            self.storage.remove_product(product, qtd)

    def add_product_to_cart(self, product, qtd=1):
        if self.storage.search_product(product.name) is None:
            return False
        
        self.storage.remove_product(product, qtd)
        self.cart.add_product(product, qtd)

    def remove_product_from_cart(self, product):
        if self.cart.search_product(product.name) is None:
            return False
        
        self.cart.remove_product(product)
        self.storage.add_product(product)

    def total_cart(self):
        return self.cart.total()
    
    def get_cart(self):
        return self.cart.get_products()
    
    def get_storage(self):
        return self.storage.get_products()
    

