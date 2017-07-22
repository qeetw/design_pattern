from abc import ABCMeta, abstractmethod
from beverage import Beverage

class CondimentDecorator(Beverage, metaclass=ABCMeta):
    @abstractmethod
    def get_description(self):
        pass