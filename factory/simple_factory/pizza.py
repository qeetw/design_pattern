from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass
    
    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

class CheesePizza(Pizza):
    def __init__(self):
        self.name = "CheesePizza"

    def get_name(self):
        return self.name

    def prepare(self):
        print("CheesePizza prepare")

    def bake(self):
        print("CheesePizza bake")
    
    def cut(self):
        print("CheesePizza cut")

    def box(self):
        print("CheesePizza box")

class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "PepperoniPizza"

    def get_name(self):
        return self.name

    def prepare(self):
        print("PepperoniPizza prepare")

    def bake(self):
        print("PepperoniPizza bake")
    
    def cut(self):
        print("PepperoniPizza cut")

    def box(self):
        print("PepperoniPizza box")

class ClamPizza(Pizza):
    def __init__(self):
        self.name = "ClamPizza"

    def get_name(self):
        return self.name

    def prepare(self):
        print("ClamPizza prepare")

    def bake(self):
        print("ClamPizza bake")
    
    def cut(self):
        print("ClamPizza cut")

    def box(self):
        print("ClamPizza box")