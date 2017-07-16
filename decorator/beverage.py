from abc import ABCMeta, abstractclassmethod

class Beverage(metaclass=ABCMeta):
    description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractclassmethod
    def cost(self):
        pass