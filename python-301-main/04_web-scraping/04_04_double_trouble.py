# Research for interesting APIs online and pick two. You can also use APIs that
# you've already worked with in the course if you prefer.
# Write a program that makes calls to both APIs and find a way to combine the
# data that you receive from both of them.
# E.g.: You could use the Ghibli API to find all ghosts from their films, and
#       create an opposing team of Ghost Pokémon from the Poke API.

import requests
from random import randint

# API to check weather conditions if weather is cloudy depending on the location of the user
def weather(lat,lon):
    API_key="ab429330748f508db5b61e5e5e22dfd1"
    base_url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(base_url)
    resp_lan=response.json()
    if resp_lan["weather"][0]["main"]=="Clouds":
        cloud=True
    else:
        cloud=False
    return cloud



latitude=input("Please enter the latitude of your position (You can check it on Google maps: ")
longitude=input("Please enter the longitude of your position: ")

num = randint(1,150)

BASE_URL = "https://pokeapi.co/api/v2/"   #https://pokeapi.co/api/v2/gender/1/

page = requests.get(BASE_URL+"pokemon/1/")  # It`s directly getting the info as a string no html`
page1=page.json()

page = requests.get(BASE_URL+"pokemon/"+str(num)+"/")  # It`s directly getting the info as a string no html`
page1=page.json()
name=page1["name"]
id=page1["id"]

if page1["types"][0]["type"]["name"]=="water" and weather(latitude,longitude)==True:
    print("Be careful seems that soon it`s going to rain")

else:
    print("Don`t worry, seems that the weather will be good")