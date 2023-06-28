# Use the Pokemon API at https://pokeapi.co/ to assemble a team of your
# six favorite Pokémon.
# Your task is to fetch information about six Pokémon through the
# necessary API calls and include the information in your local script.
# This information should include at least:
# - name
# - number
# - types
#
# You can improve on your project even more by writing the data to a small
# `.html` page which allows you to also display the sprites of each Pokémon.
# Check out the guides they provide: https://pokeapi-how.appspot.com/page5   # I get server error


import requests
from bs4 import BeautifulSoup

BASE_URL = "https://pokeapi.co/api/v2/"   #https://pokeapi.co/api/v2/gender/1/

page = requests.get(BASE_URL+"pokemon/1/")  # It`s directly getting the info as a string no html`
page1=page.json()
#soup = BeautifulSoup(page.text)

for i in range(1,7,1):
    page = requests.get(BASE_URL+"pokemon/"+str(i)+"/")  # It`s directly getting the info as a string no html`
    page1=page.json()
    name=page1["name"]
    id=page1["id"]
    print(f"the name of this pokemon is {name}")
    print(f"the id of this pokemon is {id}")
    if len(page1["types"])==1:
        type1=page1["types"][0]["type"]["name"]
        print(f"The type of this pokemon is {type1}.")
        print("\n")
    elif len(page1["types"])==2:
        type1=page1["types"][0]["type"]["name"]
        type2=page1["types"][1]["type"]["name"]
        print(f"The types it has are {type1} and {type2}")
        print("\n")


