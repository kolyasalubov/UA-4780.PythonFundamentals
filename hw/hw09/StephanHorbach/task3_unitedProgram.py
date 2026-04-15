import tkinter as tk
from pyowm import OWM
from pyowm.utils.config import get_default_config

HEIGHT = 350
WIDTH  = 450

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

def get_weather():
    city = entry_field.get().strip()
    if not city:
        label.config(text="Please enter a city name.", bg="tomato", fg="white")
        return

    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(city)
        w = observation.weather

        status      = w.detailed_status.capitalize()
        wind        = w.wind()
        humidity    = w.humidity
        temp        = w.temperature('celsius')
        clouds      = w.clouds
        rain        = w.rain if w.rain else "None"

        result = (
            f"City:        {city}\n"
            f"Status:      {status}\n"
            f"Temp:        {temp.get('temp', 'N/A'):.1f} °C\n"
            f"Temp min:    {temp.get('temp_min', 'N/A'):.1f} °C\n"
            f"Temp max:    {temp.get('temp_max', 'N/A'):.1f} °C\n"
            f"Humidity:    {humidity} %\n"
            f"Wind speed:  {wind.get('speed', 'N/A')} m/s\n"
            f"Clouds:      {clouds} %\n"
            f"Rain:        {rain}"
        )

        label.config(text=result, bg="white", fg="black", anchor="w", justify="left")

    except Exception as e:
        label.config(
            text=f"Error: {str(e)}",
            bg="tomato", fg="white",
            anchor="center", justify="center"
        )

# ── UI Setup ──────────────────────────────────────────────────────
root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Search bar frame
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry_field.insert(0, "London,GB")  # default hint

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Results frame
lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12),
                 text="Enter a city and press Get Weather",
                 bg="white", anchor="w", justify="left",
                 wraplength=280, padx=8)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()