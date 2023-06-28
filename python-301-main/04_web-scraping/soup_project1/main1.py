from class_ing import Ingredient , Spice,Soup,Recipe_Cod_Nomads

lista=""
list_ing=[]
list_spice=[]
text=None
error=None

while text!="exit":
    print("If you want to write a ingredient just type it, to exit type 'exit'")
    text=input("please write the ingredient you want or 'exit': \n")
    if text!="exit":
        lista+=text+" "
        list_ing.append(text.lower())
    else:
        break

text=None

while text!="exit":
    print("If you want to write a spice just type it, to exit type 'exit'")
    text=input("please write the spice you want or 'exit': \n")
    if text!="exit":
        lista+=text+" "
        list_spice.append(text.lower())
    else:
        break

#print(list_ing)
#print(list_spice)
Recipe_Cod_Nomads.write_file("/Users/sagar/OneDrive/Escritorio",Recipe_Cod_Nomads.soup_web("https://codingnomads.github.io/recipes/"))
print(Recipe_Cod_Nomads.read_file("/Users/sagar/OneDrive/Escritorio",list_ing))
#Soup.cook(lista)
Recipe_Cod_Nomads.Web_Browser("https://codingnomads.github.io/recipes/",Recipe_Cod_Nomads.read_file("/Users/sagar/OneDrive/Escritorio",list_ing))

