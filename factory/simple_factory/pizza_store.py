class PizzaStore():
    def __init__(self, factory):
        self.factory = factory
    
    def order_pizza(self, type):
        pizza = self.factory.create_pizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
        