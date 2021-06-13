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

    def __str__(self, name, quantity, price, speed_of_scanning):
        try:
            self.quantity = int(self.quantity)
            return {'name': self.name, 'quantity': self.quantity, 'price': self.price, 'speed_of_scanning': self.speed_of_scanning}
        except:
            raise ValueError("Неправильно")
# Не понимаю, почему не работает - он не видит аргументы, но они есть!

class Printers(Technics):

    def __init__(self, name, quantity, price, speed_of_printing):
        super().__init__(name, quantity, price)
        self.speed_of_printing = speed_of_printing



class Xeroxes(Technics):

    def __init__(self, name, quantity, price, speed_of_xerox):
        super().__init__(name, quantity, price)
        self.speed_of_xerox = speed_of_xerox


xe = Xeroxes('Xerox_1', 3, 4, 2)
print(xe.__dict__)

printer_1 = Printers('Printer_1', 4, 3, 6)
print(printer_1.__dict__)

scaner_1 = Scaners('Scaner_1', 8, 6, 3)
print(scaner_1)