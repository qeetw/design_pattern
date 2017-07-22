from abc import ABCMeta, abstractmethod, abstractproperty

class Pizza(metaclass=ABCMeta):
    def __init__(self):
        self.name = 'pizza'
        self.dough = 'pizza dough'
        self.sauce = 'pizza sauce'
        self.toppings = []

    def prepare(self):
        print('Preparing', self.name)
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings:')
        for topping in self.toppings:
            print('\t', topping, end=' ')
        print()

    def bake(self):
        print('Bake for 25 minutes at 350')
    
    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name 