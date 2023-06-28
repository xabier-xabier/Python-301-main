# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

class Pokemon:

    def __init__(self,name,primary_type,max_hp,hp):
        self.name=name
        self.primary_type=primary_type
        self.max_hp=max_hp
        self.hp=hp
        pass

    def __str__(self):
        return f""" 
                The pokemon {self.name} has a primary type of {self.primary_type}
                a maximum hp of {self.max_hp} and a actual hp of {self.hp}"""
    
    def feed(self):
        print(f"{self.name} has been feed with 10hp")
        self.hp+=10
        pass

    def battle1(self,other):
        print(f"there is battle bewteen {self.name} and {other.name}")
        result=Pokemon.typewheel(self.primary_type,other.primary_type)
        print(f"{self.name} fought {other.name} and the result is {result}")
        #call decision

    def typewheel(type1,type2):
        result={0:"win", 1:"lose",-1:"draw"}
        game_map={"water":0, "fire":1, "grass":2}
        # win-lose matrix
        wl_matrix=[
            [-1,1,0],   #water
            [1,-1,0],   #fire
            [0,1,-1],   #grass
        ]
        wl_result=wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]

    
    def battle(self,other):

        if self.primary_type=="water" and other.primary_type=="fire":
            print(f"{self.name} won the battle")
            print(f"{other.name} lost 15 hp")
            other.hp-=15

        elif self.primary_type=="water" and other.primary_type=="grass":
            print(f"{other.name} won the battle")
            print(f"{self.name} lost 15 hp")
            self.hp-=15

        elif self.primary_type=="fire" and other.primary_type=="grass":
            print(f"{self.name} won the battle")
            print(f"{other.name} lost 15 hp")
            other.hp-=15

        elif self.primary_type=="fire" and other.primary_type=="water":
            print(f"{other.name} won the battle")
            print(f"{self.name} lost 15 hp")
            self.hp-=15

        elif self.primary_type=="grass" and other.primary_type=="water":
            print(f"{self.name} won the battle")
            print(f"{other.name} lost 15 hp")
            other.hp-=15

        else:
            print(f"{other.name} won the battle")
            print(f"{self.name} lost 15 hp")
            self.hp-=15



r1=Pokemon("Pedro","grass",100,100)
r2=Pokemon("Juanjo","water",100,100)

Pokemon.battle(r1,r2)
print(r2.hp)

Pokemon.battle1(r1,r2)
print(Pokemon.typewheel(r1.primary_type,r2.primary_type))
#r1.battle1(r2)
#Pokemon.feed(r2)
#print(r2.hp)
