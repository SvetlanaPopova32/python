class Store:
    pass

class Technics:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Scaners(Technics):

    def __init__(self, name, quantity, price, speed_of_scanning):
        super().__init__(name, quantity, price)
        self.speed_of_scanning = speed_of_scanning



class Printers(Technics):

    def __init__(self, name, quantity, price, speed_of_printing):
        super().__init__(name, quantity, price)
        self.speed_of_printing = speed_of_printing



class Xeroxes(Technics):

    def __init__(self, name, quantity, price, speed_of_xerox):
        super().__init__(name, quantity, price)
        self.speed_of_xerox = speed_of_xerox


xe = Xeroxes(2, 3, 4, 2)
print(xe.__dict__)

