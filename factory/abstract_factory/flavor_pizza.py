from pizza import Pizza

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredient_factory = ingredientFactory

    def prepare(self):
        print('Preparing', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        print('dough:', self.dough)
        print('sauce:', self.sauce)
        print('cheese:', self.cheese)                

class ClamPizza(Pizza):
    def __init__(self, ingredientFactory):
        self.ingredient_factory = ingredientFactory

    def prepare(self):
        print('Preparing', self.name)
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_cheese()
        print('dough:', self.dough)
        print('sauce:', self.sauce)
        print('cheese:', self.cheese)
        print('clam:', self.clam)