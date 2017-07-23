from enum import Enum

class CellingFan():
    class Speed(Enum):
        OFF = 0
        LOW = 1
        HIGH = 2

    def __init__(self):
        self.speed = CellingFan.Speed.OFF

    def off(self):
        self.speed = CellingFan.Speed.OFF
        print('Celling Fan is Off')

    def low(self):
        self.speed = CellingFan.Speed.LOW
        print('Celling Fan is Low')

    def high(self):
        self.speed = CellingFan.Speed.HIGH
        print('Celling Fan is HIGH')

    def get_speed(self):
        return self.speed