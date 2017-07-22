from pizza import Pizza

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings = ['Grated Reggiano Cheese']

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'NY Style Pepperoni Pizza'
        self.dough = 'NY Pepperoni Dough'
        self.sauce = 'NY Pepperoni Sauce'
        self.toppings = ['NY Pepperoni Cheese']

class NYStyleClamPizza(Pizza):
    def __init__(self):
        self.name = 'NY Style Clam Pizza'
        self.dough = 'NY Clam Dough'
        self.sauce = 'NY Clam Sauce'
        self.toppings = ['NY Clam Cheese']