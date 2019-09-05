class Item:
    def __init__(self):
        self.name = []
        self.price = []

    def add_product(self,product):
        self.name.append(product)

    def add_price(self,price):
        self.price.append(price)