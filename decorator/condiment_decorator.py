from abc import ABCMeta, abstractclassmethod
from beverage import Beverage

class CondimentDecorator(Beverage, metaclass=ABCMeta):
    @abstractclassmethod
    def get_description(self):
        pass