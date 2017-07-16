from condiment_decorator import CondimentDecorator
from beverage import Beverage

class Mocha(CondimentDecorator):
    beverage = None

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return round(0.20 + self.beverage.cost(), 2)