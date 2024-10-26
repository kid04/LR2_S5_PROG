from owm_key import owm_api_key
from getweatherdata import get_weather_data

if __name__ == '__main__':
    get_weather_data('Chicago', api_key=owm_api_key)
    get_weather_data('Saint Petersburg', api_key=owm_api_key)
    get_weather_data('Dhaka', api_key=owm_api_key)