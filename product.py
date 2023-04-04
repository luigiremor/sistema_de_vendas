class Product:

    def __init__(self, name, price, qtd) -> None:
        self.name = name
        self.price = price
        self.qtd = qtd

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_qtd(self):
        return self.qtd
    
    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
    
    def set_qtd(self, qtd):
        self.qtd = qtd
    
    def __str__(self) -> str:
        return f"Nome: {self.name} - Preço: {self.price} - Quantidade: {self.qtd}"
    
    def __repr__(self) -> str:
        return f"{self.name} - {self.price} - {self.qtd}"
