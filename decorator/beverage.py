from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):
    description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass
