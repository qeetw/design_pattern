from condiment_decorator import CondimentDecorator
from beverage import Beverage

class Whip(CondimentDecorator):
    beverage = None

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return round(0.30 + self.beverage.cost(), 2)