from pizza import Pizza

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings = ['Shredded Mozzarella Cheese']

    def cut(self):
        print('Cutting the pizza into square slices')


class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Pepperoni Pizza'
        self.dough = 'Chicago Pepperoni Dough'
        self.sauce = 'Chicago Pepperoni Sauce'
        self.toppings = ['Chicago Pepperoni Cheese']


class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        self.name = 'Chicago Style Clam Pizza'
        self.dough = 'Chicago Clam Dough'
        self.sauce = 'Chicago Clam Sauce'
        self.toppings = ['Chicago Clam Cheese']
