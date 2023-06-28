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


class Spice:
    """Models a spice to flavor your food."""

    def __init__(self, name, taste):
        self.name=name
        self.taste = taste

    def expire(self):
        print(f"your {self.name} has expired. it's probably still good.")
        self.name = "old " + self.name

    def grind(self):
        print(f"You have now {self.taste} of ground {self.name}.")

class Soup():

    def soup_web(*args): # I need to add args here to add as many ingredients and spices as possible
        base_url="https://www.edamam.com/results/recipes/?search="
        for i in args:
            base_url+=i

        webbrowser.open(base_url)
        pass


