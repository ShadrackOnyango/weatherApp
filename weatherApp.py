import requests
import json
import datetime

def is_daytime():
    now = datetime.datetime.now()
    start_time = datetime.time(6, 0, 0)
    end_time = datetime.time(18, 0, 0)
    current_time = datetime.time(now.hour, now.minute, now.second)
    return start_time <= current_time <= end_time

API_KEY = "06d3ce0088c8b191c357ba822e3912b8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the name of the city: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(url)
data = json.loads(response.text)

if "weather" in data:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"The current time in {city} is {current_time}")
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    temperature_celsius = temperature_kelvin - 273
    humidity = data["main"]["humidity"]

    if weather == "Rain":
        print("It's raining. You might want to stay indoors and enjoy a book or a movie.")
    else:
        if temperature_celsius >= 30:
            if is_daytime():
                print("It's hot outside! You can go for a swim or enjoy some ice cream.")
            else:
                print("It's hot outside! Consider finding shade or staying in a cool place.")
        elif temperature_celsius >= 20:
            if is_daytime():
                print("The weather is pleasant. It's a good time for outdoor activities.")
            else:
                print("The weather is pleasant. You can relax and enjoy the evening.")
        elif temperature_celsius >= 10:
            if is_daytime():
                print("It's a bit chilly. Consider wearing a light jacket and going for a walk.")
            else:
                print("It's a bit chilly. You can cozy up indoors with a warm drink.")
        else:
            print("It's cold outside. Stay warm and cozy indoors.")

    print(f"Weather in {city}:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature_celsius} °C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
else:
    print(f"Weather information for {city} is not available.")
