from abc import ABCMeta, abstractmethod

class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass