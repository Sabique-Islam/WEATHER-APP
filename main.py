import requests
import json
import pyttsx3

print("WEATHER APP VERSION 1.0 by Sabique...")
name = input("Enter name of city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=3a398cbf402f4d0a8ab155311242309&q={name}"
receive = requests.get(url)
r = receive.text
#print(r) #SHOWS ALL THE DETAILS
weatherdata = json.loads(r)
x = weatherdata["current"]["temp_c"]
print("TEMPERATURE:-", x, "°C")

print("Do you want a voice note?")
ask = input("YES/NO:- ")
if ask.upper() == "YES":
    x =f"TEMPERATURE in {name} is {x} °C "
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
