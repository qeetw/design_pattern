from observer import Observer
from weather_data import WeatherData

class CurrentConditionDisplay(Observer):
    temperature = None
    humidity = None
    pressure = None

    def update(self, observable_obj):
        if isinstance(observable_obj, WeatherData):
            self.temperature = observable_obj.get_temperature()
            self.humidity = observable_obj.get_humidity()
            self.pressure = observable_obj.get_pressure()
            self.display()

    def display(self):
        print('**** Current Condition ****')
        print('temperature:', self.temperature)
        print('humidity:', self.humidity)
        print('pressure:', self.pressure)