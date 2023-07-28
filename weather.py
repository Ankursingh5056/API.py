import requests

# Enter Your API Key
API_KEY = "0acccca72fc27ffb6afa51b000fbfeb6"

# Enter Your Native_City
city = input("Enter your city Name :")

# Enter the Required URL
url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=0acccca72fc27ffb6afa51b000fbfeb6&units=metric".format(city)


res = requests.get(url)
data = res.json()

temperature = data["main"]["temp"]
print(f"temperature in {city} is {temperature} deg. celsius")

# My code is Ready to see weather report
