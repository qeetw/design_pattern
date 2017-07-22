from pizza_store import PizzaStore
from chicago_style_pizza import ChicagoStyleCheesePizza, ChicagoStylePepperoniPizza, ChicagoStyleClamPizza

class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None

        if type == 'cheese':
            pizza = ChicagoStyleCheesePizza()
        elif type == 'pepperoni':
            pizza = ChicagoStylePepperoniPizza()
        elif type == 'clam':
            pizza = ChicagoStyleClamPizza()

        return pizza