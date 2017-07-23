from abc import ABCMeta, abstractmethod
from light import Light
from celling_fan import CellingFan

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class NoCommand(Command):
    def execute(self):
        print('No Command Execute')
    
    def undo(self):
        print('No Command Undo')

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()

class CellingFanHighCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.pre_speed = self.fan.get_speed()
        self.fan.high()
    
    def undo(self):
        if self.pre_speed == CellingFan.Speed.HIGH:
            self.fan.high()
        elif self.pre_speed == CellingFan.Speed.LOW:
            self.fan.low()
        elif self.pre_speed == CellingFan.Speed.OFF:
            self.fan.off()

class CellingFanLowCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.pre_speed = self.fan.get_speed()
        self.fan.low()
    
    def undo(self):
        if self.pre_speed == CellingFan.Speed.HIGH:
            self.fan.high()
        elif self.pre_speed == CellingFan.Speed.LOW:
            self.fan.low()
        elif self.pre_speed == CellingFan.Speed.OFF:
            self.fan.off()

class CellingFanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.pre_speed = self.fan.get_speed()
        self.fan.off()
    
    def undo(self):
        if self.pre_speed == CellingFan.Speed.HIGH:
            self.fan.high()
        elif self.pre_speed == CellingFan.Speed.LOW:
            self.fan.low()
        elif self.pre_speed == CellingFan.Speed.OFF:
            self.fan.off()