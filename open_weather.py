import requests

# Your OpenWeatherMap API key
api_key = "aa746349d657f9cadd9f173eb7610bf0"

# The city for which you want to fetch the weather information
city = "Львів"

# Make a GET request to the OpenWeatherMap API
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ua")

# Extract the weather information from the JSON response
weather_data = response.json()
print(weather_data)

# Extract the temperature in Kelvin
temperature = weather_data['main']['temp']


# # Convert the temperature to Celsius
# temperature_in_celsius = temperature - 273.15


# Extract the weather description
weather_description = weather_data['weather'][0]['description']


# Extract the wind speed
wind_speed = weather_data['wind']['speed']


# Extract the humidity
humidity = weather_data['main']['humidity']


# Use the extracted information to display the weather information to the user
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather_description}")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Humidity: {humidity}%")