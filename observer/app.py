from weather_data import WeatherData
from current_condition_display import CurrentConditionDisplay

def main():
    weather_data = WeatherData()
    current_condition_display = CurrentConditionDisplay()

    weather_data.add_observer(current_condition_display)
    weather_data.set_measurements(10, 12, 30)
    weather_data.set_measurements(50, 60, 70)
    weather_data.delete_observer(current_condition_display)
    weather_data.set_measurements(100, 200, 300)

if __name__ == '__main__':
    main()