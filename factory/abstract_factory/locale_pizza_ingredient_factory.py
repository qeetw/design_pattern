from pizza_ingredient_factory import PizzaIngredientFactory

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'NY dough'

    def create_sauce(self):
        return 'NY sauce'

    def create_cheese(self):
        return 'NY cheese'

    def create_veggies(self):
        return ['NY veggies']

    def create_pepperoni(self):
        return 'NY pepperoni'

    def create_clam(self):
        return 'NY clam'

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return 'Chicago dough'

    def create_sauce(self):
        return 'Chicago sauce'

    def create_cheese(self):
        return 'Chicago cheese'

    def create_veggies(self):
        return ['Chicago veggies']

    def create_pepperoni(self):
        return 'Chicago pepperoni'

    def create_clam(self):
        return 'Chicago clam'