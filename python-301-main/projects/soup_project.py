import webbrowser

class Ingredient:

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
        pass

    def get_info(self):
        url="https://en.wikipedia.org/wiki/"+self.name
        webbrowser.open_new(url)
        pass

name=input("enter the fruit name: ")
amount=int(input("write the amount please: "))

fruit=Ingredient(name,amount)

print(fruit.name)

fruit.get_info()