
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5, 1)

class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3, 1)

coat = Coat(20)
suit = Suit(35)
print(coat.calculate)
print(suit.calculate)
