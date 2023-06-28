import webbrowser

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient):
    """Models a spice to flavor your food."""

    def __init__(self, name, amount,taste):
        super().__init__(name, amount)
        self.taste=taste

    def expire(self):
        print(f"your {self.name} has expired. it's probably still good.")
        self.name = "old " + self.name

    def grind(self):
        print(f"You have now {self.taste} of ground {self.name}.")

class Soup():

    def __init__(self,name):
        self.name= name
        pass

    def cook(*args): # I need to add args here to add as many ingredients and spices as possible
        base_url="https://www.edamam.com/results/recipes/?search="
        for i in args:
            base_url+=i+" "

        webbrowser.open(base_url)
        pass

    def use_API(*args):
        #self.args= args
        #self.spice= args
        pass


    #def cook():


if __name__ == "__main__":

    r1=Ingredient("carrot",10)
    r2=Spice("Chili",10,"sweet")
    r3=Ingredient("pasta",2)

    r2=Soup.cook(r1.name,r2.name,r3.name)


