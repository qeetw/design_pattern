from observable import Observable

class WeatherData(Observable):
    temperature = 20
    humidity = 50
    pressure = 0.9

    def get_temperature(self):
        return self.temperature
    
    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self. pressure = pressure
        self.measurements_changed()

    def measurements_changed(self):
        self.set_changed()
        self.notify_observers()