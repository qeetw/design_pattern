from pizza_store import PizzaStore
from locale_pizza_ingredient_factory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from flavor_pizza import CheesePizza, ClamPizza

class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None
        ingredientFactory = NYPizzaIngredientFactory()

        if type == 'cheese':
            pizza = CheesePizza(ingredientFactory)
            pizza.set_name('NY Style Cheese Pizza')
        elif type == 'clam':
            pizza = ClamPizza(ingredientFactory)
            pizza.set_name('NY Style Clam Pizza')

        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None
        ingredientFactory = ChicagoPizzaIngredientFactory()

        if type == 'cheese':
            pizza = CheesePizza(ingredientFactory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif type == 'clam':
            pizza = ClamPizza(ingredientFactory)
            pizza.set_name('Chicago Style Clam Pizza')

        return pizza