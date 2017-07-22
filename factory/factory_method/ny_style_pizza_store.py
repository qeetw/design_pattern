from pizza_store import PizzaStore
from ny_style_pizza import NYStyleCheesePizza, NYStylePepperoniPizza, NYStyleClamPizza

class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None

        if type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif type == 'pepperoni':
            pizza = NYStylePepperoniPizza()
        elif type == 'clam':
            pizza = NYStyleClamPizza()

        return pizza