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

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def expire(self):
        print(f"your {self.name} has expired. it's probably still good.")
        self.name = "old " + self.name

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")


c = Ingredient("carrots", 2)
p = Spice("pepper", 2, "hot")
p.expire()
print(c, p)