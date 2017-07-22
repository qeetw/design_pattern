from abc import ABCMeta, abstractmethod

class PizzaStore(metaclass=ABCMeta):
    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type):
        pass
        