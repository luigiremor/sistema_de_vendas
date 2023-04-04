from product import Product


class Cart:
    def __init__(self):
        self.products: dict[str, Product] = {}

    def add_product(self, product, qtd=1):
        if product.name in self.products.keys():
            self.products[product.name].qtd += qtd
        else:
            product = Product(product.name, product.price, qtd) 
            self.products[product.name] = product

    def remove_product(self, product, qtd=1):
        if product.name in self.products.keys():
            self.products[product.name].qtd -= qtd
            if self.products[product.name].qtd <= 0:
                del self.products[product.name]

    def search_product(self, name):
        if name in self.products.keys():
            return self.products[name]
        else:
            return None

    def total(self):
        total = 0
        for product in self.products.values():
            total += product.price * product.qtd
        return total
    
    def get_products(self):
        return self.products.values()
    
    def __str__(self) -> str:
        return f"Produtos: {self.get_products()} - Total: {self.total()}"    