from class_ing import Ingredient , Spice,Soup

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
        list_ing.append(text)
    else:
        break

text=None

while text!="exit":
    print("If you want to write a spice just type it, to exit type 'exit'")
    text=input("please write the spice you want or 'exit': \n")
    if text!="exit":
        lista+=text+" "
        list_spice.append(text)
    else:
        break


Soup.soup_web(lista)


