# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Football_Team:

    def __init__(self,name,titles,supporters):
        self.name=name
        self.titles=titles
        self.supporters=supporters
        pass

    def __str__(self):
        return f"""
            The {self.name} won {self.titles} titles since its
            creation and has {self.supporters} supporters"""
        pass

    def __add__(self,other):
        new_name=f" {self.name}+{other.name} together"
        amount_titles=self.titles+other.titles
        new_supporter=self.supporters+other.supporters
        return Football_Team(new_name,amount_titles,new_supporter)
    
class Football_boots:
     
     def __init__(self,cost,size,brand):
         self.cost=cost
         self.size=size
         self.brand=brand
         pass
     
     def __str__(self):
         return f""" 
            The {self.brand} brand of boots has a cost of {self.cost} Euros
                        and you can find size up to {self.size}"""
        
     
class Football_t_shirts:

    def __init__(self,name,color,size,cost):
        self.name=name
        self.color=color
        self.size=size
        self.cost=cost
        pass

    def __str__(self):
        return f""" 
            The color of the {self.name} football team t-shirt is {self.color}
            you can find t-shirts up to size {self.size} at the official shop
                        and the cost is {self.cost} Euros."""



real_madrid=Football_Team("Real Madrid FC",77,180000)
barcelona=Football_Team("Barcelona FC",68,150000)

s=real_madrid+barcelona
print(real_madrid,"\n")
print(barcelona,"\n")
print(s)

real_madrid_t_shirt=Football_t_shirts("Real Madrid","white","XXL",70)
adidas_boots=Football_boots(220,48,"Adidas")

print(real_madrid_t_shirt,"\n")
print(adidas_boots)
