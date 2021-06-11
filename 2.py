from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):

    def __init__(self, V):
        self.V = V

    @property
    def fabric(self):
        return self.V / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, H):
        self.H = H

    @property
    def fabric(self):
        return 2*self.H + 0.3

coat_1 = Coat(45)
costume_1 = Costume(67)
print(coat_1.fabric + costume_1.fabric)





