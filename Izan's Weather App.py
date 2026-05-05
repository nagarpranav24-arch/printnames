import requests
API_key = "a30d257dda4b6ca72ff8946f0448cba8"
country = input("write the country name that you want to see it's city's temperate")
place = input("write the city name that you want to see the temperature")
# URL = "https://api.openweathermap.org/data/2.5/onecall?{County}=33.44&{City}=-94.04&exclude=current,minutely,hourly,daily&appid={API_key}"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={place},{country}&APPID={API_key}&units={'metric'}"

def weather():
    print("Welcome to Izan's weather App")

    
   
    

    response = requests.get(URL)
    data = response.json()
    temp_data = data['main']['temp']
    humidity_data=data['main']['humidity']
    clouds = data["clouds"]["all"]
    wind_speed = data["wind"]["speed"]
    # temp = temp_data[temp]
    # print(temp_data)
    # print(humidity_data)
    # print(wind_speed)
    print(f""" The temperuture in {country}'s city {place} is {temp_data}
    with sky clouds {clouds} wind speed {wind_speed} 
    And humidity {humidity_data}%""")
    
    
weather()