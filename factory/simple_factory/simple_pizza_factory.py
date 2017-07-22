from pizza import CheesePizza, PepperoniPizza, ClamPizza

class SimplePizzaFactory():
    def create_pizza(self, type):
        pizza = None

        if type == "cheese":
            pizza = CheesePizza()
        elif type == "pepperoni":
            pizza = PepperoniPizza()
        elif type == "clam":
            pizza = ClamPizza()

        return pizza 