from duck import Duck
from quack import Quack
from fly_with_wings import FlyWithWings

class MallardDuck(Duck):
    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()

    def swin(self):
        print('Mallar Duck Swin')

    def display(self):
        print('Mallar Duck Display')
