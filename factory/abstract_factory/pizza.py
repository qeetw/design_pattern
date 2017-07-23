from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    def __init__(self):
        self.name = 'pizza'
        self.dough = 'pizza dough'
        self.sauce = 'pizza sauce'
        self.veggies = ['pizza veggies']
        self.cheese = 'pizza cheese'
        self.pepperoni = 'pizza pepperoni'
        self.clam = 'pizza clam'

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')
    
    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name