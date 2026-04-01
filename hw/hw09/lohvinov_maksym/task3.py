import tkinter as tk
from pyowm import OWM  

def get_weather():
    owm = OWM('ef2206ff5da67de63306d0b143e20872') 
    mgr = owm.weather_manager()
    
    city = city_field.get()
    w = mgr.weather_at_place(city).weather
    temp = w.temperature('celsius')['temp']
    
    my_label.config(text=f"Температура: {temp}°C")


root = tk.Tk()
root.title("Моя погода")
root.geometry("300x400")

city_field = tk.Entry(root)
city_field.pack()

my_button = tk.Button(root, text="Дізнатись погоду", command=get_weather)
my_button.pack()

my_label = tk.Label(root, text="Тут буде відповідь")
my_label.pack()

root.mainloop()