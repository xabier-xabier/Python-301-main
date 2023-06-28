from random import randint
import time
from class_ import Hero, Oponent,Wolves,Final_Oponent



loc=1
medicine=False
# Hero player
player=Hero("xabi","sword",100)

# Oponents
angelus=Oponent("The librarian","baseball bat",80)
bisontus=Oponent("The Bison","Hands",90)
ear_plucker=Oponent("Ear chopper","bowie knife",95)
the_driller=Oponent("Mr driller","drill",100)

#Final oponents
Wolves_oponent=Wolves("Herd of wolves","sharp teeth",30,10)
Final_oponent=Final_Oponent("sharpy Johnny","chainsaw",100,10)

#choose your own name and habilities
text=input("choose a name: ")
player.name=text
text1=input("Choose your main strenght: ")
player.main_strength=text1

print(type(player.hp))

while player.hp>0 or Wolves_oponent.alive_check()==True:
    print(f"your hp level is {player.hp}")
    print(f"The wolves hp is {Wolves_oponent.hp}")
    if Wolves_oponent.alive_check()==True and player.hp>0:
        fight_wolves=Wolves_oponent.attack()
        if fight_wolves==True and player.hp>0:
            player.battle_run_wolves(Wolves_oponent)
            print(f"your hp level is {player.hp}")
            print(f"The wolves hp is {Wolves_oponent.hp}")
        else:
            player.battle(Wolves_oponent)
            print(f"your hp level is {player.hp}")
            print(f"The wolves hp is {Wolves_oponent.hp}")
    #Wolves_oponent.alive_check()

if Wolves_oponent.alive_check()==True:
    print(f"Congratulations you beat {Wolves_oponent.name}")
    print(f"Now it`s turn for {Final_oponent.name}")

while player.hp>0 or Final_oponent.alive_check()==True :
    print(f"your hp level is {player.hp}")
    print(f"The {Final_oponent.name} hp is {Final_oponent.hp}")
    if Final_oponent.alive_check()==True and player.hp>0:
        fight_final=Final_oponent.attack()
        if fight_final==True and player.hp>0:
            player.battle_super_attack(Final_oponent)
            print(f"your hp level is {player.hp}")
            print(f"The {Final_oponent.name} hp is {Final_oponent.hp}")
        else:
            player.battle(Final_oponent)
            print(f"your hp level is {player.hp}")
            print(f"The {Final_oponent.name} hp is {Final_oponent.hp}")
    #Wolves_oponent.alive_check()

if player.hp<=0:
    print("Game over. You lost")

else:
    print(f"Congratulations!!  {player.name} won the game")