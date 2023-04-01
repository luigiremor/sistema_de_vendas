from product import Product


class Storage:
    def __init__(self):
        self.products: dict[str, Product] = {}

    def add_product(self, product, qtd=1):
        if product.name in self.products.keys():
            self.products[product.name].qtd += qtd
        else:
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
