from random import randint
import time
from class_ import Hero, Oponent,Wolves,Final_Oponent


sum=0
loc=1
medicine=False
# Hero player
player=Hero("xabi","sword",10000)

# Oponents
angelus=Oponent("The librarian","baseball bat",80)
bisontus=Oponent("The Bison","Hands",90)
ear_plucker=Oponent("Ear chopper","bowie knife",95)
the_driller=Oponent("Mr driller","drill",100)

#Final oponents
Wolves_oponent=Wolves("Herd of wolves","sharp teeth",30,10)
Final_oponent=Final_Oponent("sharpy Johnny","chainsaw",100,10)


if __name__=="__main__":
    while angelus.alive_check()==True and player.hp>0:
        Hero.battle(player,angelus)


    while bisontus.alive_check()==True and player.hp>0:
        Hero.battle(player,bisontus)


    while ear_plucker.alive_check()==True and player.hp>0:
        Hero.battle(player,ear_plucker)

    while the_driller.alive_check()==True and player.hp>0:
        Hero.battle(player,the_driller)

    if player.hp>0:
        print(f"your hp is {player.hp}, you beated all the oponents")
        print("now it`s the final stage")

        while Wolves_oponent.alive_check()==True and player.hp>0:
            Hero.battle(player,Wolves_oponent)

        if player.hp>0:
            print(f"your hp is {player.hp}, you beated the wolves")
            print("now it`s the turn for Johnny")

            while Final_oponent.alive_check()==True and player.hp>0:
                Hero.battle(player,Final_oponent)

                if player.hp>0:
                    print(f"Congratulations {player.name}, you won")
                else:
                    print("Sorry.... Game over")

    else:
        print(f"your hp is {player.hp}, game over")



