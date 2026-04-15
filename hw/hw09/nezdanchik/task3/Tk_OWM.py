import os
import tkinter as tk
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = os.getenv('OWM_API_KEY')


def get_weather_data(city: str) -> dict[str, object]:
    owm = OWM(API_KEY)
    manager = owm.weather_manager()
    observation = manager.weather_at_place(city)
    weather = observation.weather

    return {
        "status": weather.detailed_status,
        "temperature": weather.temperature('celsius'),
        "humidity": weather.humidity,
        "wind": weather.wind(),
        "clouds": weather.clouds,
    }


def format_response(weather_data: dict[str, object]) -> str:
    temperature = weather_data["temperature"]
    wind = weather_data["wind"]
    return (
        f"Status: {weather_data['status']}\n"
        f"Temperature: {temperature['temp']} C\n"
        f"Feels like: {temperature.get('feels_like', 'n/a')} C\n"
        f"Humidity: {weather_data['humidity']}%\n"
        f"Wind speed: {wind.get('speed', 'n/a')} m/s\n"
        f"Clouds: {weather_data['clouds']}%"
    )


def get_weather() -> None:
    city = entry_field.get().strip()
    if not city:
        label['text'] = 'Enter a city name'
        return

    try:
        weather_data = get_weather_data(city)
        label['text'] = format_response(weather_data)
    except Exception:
        label['text'] = 'Unable to get weather for this city'


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

