from abc import ABCMeta, abstractmethod
from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior

class Duck(metaclass=ABCMeta):
    @abstractmethod
    def swin(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def performFly(self):
        self.fly_behavior.fly()
    
    def performQuack(self):
        self.quack_behavior.quack()
    
    def setFlyBehavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def setQuackBehavior(self, quack_behavior):
        self.quack_behavior = quack_behavior
