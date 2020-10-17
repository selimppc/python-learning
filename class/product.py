class Product:

    def __init__(self, price):
        # behave as regular property price
        self.price = price

    # adding property decorator to call price.
    @property
    def price(self):
        return self.__price

    # price setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price = value


product = Product(50)
print(product.price)
