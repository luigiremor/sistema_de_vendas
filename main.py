from cashier import Cashier
from manager import Manager
from cart import Cart
from product import Product
from sistema import Sistema
from storage import Storage


loja = Sistema()

cashier = Cashier()

storage = Storage()

cashier.create("Joao", "123")

is_authenticated = cashier.authenticate("Joao", "123")

loja.add_user(cashier)

loja.add_storage(cashier)

print(is_authenticated)


