from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather_data(city):#last lines of code was modified as function
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        wind = w.wind()['speed']
        
        return f"City: {city}\nStatus: {status}\nTemp: {temp}°C\nWind: {wind} m/s"
    except Exception:
        return "Error: City not found"



