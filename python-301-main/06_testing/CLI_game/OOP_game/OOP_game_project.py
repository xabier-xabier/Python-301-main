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


#choose your own name and habilities
text=input("choose a name: ")
player.name=text
text1=input("Choose your main strenght: ")
player.main_strength=text1

print("You are in a very open field, there are 2 ways pointing to south, one in the right side and another in the left")
print("You can choose to 'look' around, go to 'right south' side or 'left south' side")
print("\n")
text=input("'look', 'right south' or 'left south': ")


while text=="look":
    loc=1
    print("This room it`s empty")
    text=input("'look', 'right south' or 'left south': ")

if text=="left south":
    loc=2

elif text=="right south":
    loc=3

else:
    pass


while player.hp > 0 or sum!=4:
    
    if loc==1 and player.hp > 0 and sum!=4:
        print("This room it`s empty")
        print("You can choose to 'look' around, go to 'right' side or 'left' side\n")
        text=input("'look', 'right south' or 'left south': ")
        if text=="right south":
            loc=2
        elif text=="left south":
            loc=3
        else:
            pass

    elif loc==2 and angelus.alive_check()==True and player.hp > 0 and sum!=4:
        print("There is an oponent in this place!!")
        print(f"The fearsome {angelus.name} be careful in short distance with his {angelus.main_strength}")
        print(f"do you want to fight the mighty {angelus.name} or go to 'north', 'south' or to 'east'\n")
        print(f"your hp level is {player.hp}")
        text=input(" choose 'fight', 'north', 'south' or 'east':  ")
        if text=="fight" and angelus.alive_check()==True and player.hp > 0:
            Hero.battle(player,angelus)
            if angelus.alive_check()==False and player.hp > 0:
                print(f"{angelus.name} passed away. You beat him, one less oponent congratulationns.\n'")
                sum+=1
                while loc==2:
                    text=input("do you want to go  to 'north', 'south' or to 'east'")
                    if text=='north':
                        loc=1
                    elif text=="south":
                        loc=6
                    elif text=="east":
                        loc=4
                    else:
                        pass
            elif player.hp<=0:
                break

        elif text=="north":
            loc=1
        elif text=="south":
            loc=6
        elif text=="east":
            loc=4
        elif player.hp<=0:
            break
        elif sum==4:
            break
        else:
            pass

    
    elif loc==2 and angelus.alive_check()==False and player.hp > 0 and sum!=4:
        print(f"this room it`s empty it`s just the graveyard of {angelus.name}")
        print(f"do you want to go to 'north', 'south' or to 'left west'\n")
        text=input(" choose 'north', 'south' or 'east':  ")
        if text=="north":
            loc=1
        elif text=="south":
            loc=6
        elif text=="east":
            loc=4
        else:
            pass


    elif loc==3 and player.hp > 0 and sum!=4:
        print("This room it`s empty")
        print("You can choose to 'look' around, go to 'north','south' or go to 'west'\n")
        text=input("'look', 'north','south' or 'west': ")
        if text=="look" and medicine==False:
            print("congratulations you found a medicine kit and you gained 20hp\n")
            Hero.feed(player)
            print(f"your hp level is {player.hp}\n")
            medicine=True
        elif text=="look" and medicine==True:
            print("This place looks empty... better to move on\n")

        elif text=="north":
            loc=1
        elif text=="south":
            loc=7
        elif text=="west":
            loc=4
        elif sum==4:
            break
        else:
            pass
        
    
    elif loc==4 and player.hp > 0 and sum!=4:
        print("This place it`s really dark. It`s hard to see in here")
        print("You can choose to 'look' around, go to 'west','south' or go to 'east'\n")
        text=input("'look', 'west','south' or 'east': ")
        if text=="look":
            print("you can`t see much... looks a bit empty you will need to wait a few seconds to recover connection\n")
            time.sleep(5)
        elif text=="west":
            loc=2
        elif text=="south":
            loc=5
        elif text=="east":
            loc=3
        else:
            pass


    elif loc==5 and bisontus.alive_check()==True and player.hp > 0 and sum!=4:
        print("There is an oponent in this place!!")
        print(f"The fearsome {bisontus.name} be careful in short distance with his {bisontus.main_strength}")
        print(f"do you want to fight the mighty {bisontus.name} or go to 'north', 'south' or to 'left west'\n")
        print(f"your hp level is {player.hp}")
        text=input(" choose 'fight', 'north', 'south' or 'left west':  ")
        if text=="fight" and bisontus.alive_check()==True and player.hp > 0:
            Hero.battle(player,bisontus)
            if bisontus.alive_check()==False and player.hp > 0:
                print(f"{bisontus.name} passed away. You beat him, one less oponent congratulationns.\n'")
                sum+=1
                while loc==5:
                    text=input("do you want to go  to 'north', 'south' or to 'left west'")
                    if text=='north':
                        loc=4
                    elif text=="south":
                        loc=8
                    elif text=="left west":
                        loc=6
                    else:
                        pass
            elif player.hp<=0:
                break

        elif text=="north":
            loc=4
        elif text=="south":
            loc=8
        elif text=="left west":
            loc=6
        elif player.hp<=0:
            break
        else:
            pass

    
    elif loc==5 and bisontus.alive_check()==False and player.hp > 0 and sum!=4:
        print(f"this room it`s empty it`s just the graveyard of {bisontus.name}")
        print(f"do you want to go to 'north', 'south' or to 'left west'\n")
        text=input(" choose 'north', 'south' or 'left west':  ")
        if text=="north":
            loc=4
        elif text=="south":
            loc=8
        elif text=="left west":
            loc=6
        else:
            pass


    elif loc==6 and the_driller.alive_check()==True and player.hp > 0 and sum!=4:
        print("There is an oponent in this place!!")
        print(f"The fearsome {the_driller.name} be careful in short distance with his {the_driller.main_strength}")
        print(f"do you want to fight the mighty {the_driller.name} or go to 'north', 'east' or to 'right east'\n")
        print(f"your hp level is {player.hp}")
        text=input(" choose 'fight', 'north', 'east' or 'right east':  ")
        if text=="fight" and the_driller.alive_check()==True and player.hp > 0:
            Hero.battle(player,the_driller)
            if the_driller.alive_check()==False and player.hp > 0:
                print(f"{the_driller.name} passed away. You beat him, one less oponent congratulationns.\n'")
                sum+=1
                while loc==6:
                    text=input("do you want to go  to 'north', 'east' or to 'right east'")
                    if text=='north':
                        loc=2
                    elif text=="east":
                        loc=8
                    elif text=="right east":
                        loc=5
                    else:
                        pass
        elif player.hp<=0:
            break
        
        elif text=="north":
            loc=2
        elif text=="east":
            loc=8
        elif text=="right east":
            loc=5
        elif player.hp<=0:
            break
        else:
            pass


    elif loc==6 and the_driller.alive_check()==False and player.hp > 0 and sum!=4:
        print(f"this room it`s empty it`s just the graveyard of {the_driller.name}")
        print(f"do you want to go to 'north', 'east' or to 'right east'\n")
        text=input(" choose 'north', 'east' or 'right east':  ")
        if text=="north":
            loc=2
        elif text=="east":
            loc=8
        elif text=="right east":
            loc=5
        else:
            pass


    elif loc==7 and ear_plucker.alive_check()==True and player.hp > 0 and sum!=4:
        print("There is an oponent in this place!!")
        print(f"The fearsome {ear_plucker.name} be careful in short distance with his {ear_plucker.main_strength}")
        print(f"do you want to fight the mighty {ear_plucker.name} or go to 'north'or to 'west'\n")
        print(f"your hp level is {player.hp}")
        text=input(" choose 'fight', 'north' or 'west':  ")
        if text=="fight" and ear_plucker.alive_check()==True and player.hp > 0:
            Hero.battle(player,ear_plucker)
            if ear_plucker.alive_check()==False and player.hp > 0:
                print(f"{ear_plucker.name} passed away. You beat him, one less oponent congratulationns.\n'")
                sum+=1
                while loc==7:
                    text=input("do you want to go  to 'north' or to 'west'")
                    if text=='north':
                        loc=3
                    elif text=="west":
                        loc=8
                    else:
                        pass
            elif player.hp<=0:
                break

        elif text=="north":
            loc=3
        elif text=="west":
            loc=8
        elif player.hp<=0:
            break
        else:
            pass

    
    elif loc==7 and ear_plucker.alive_check()==False and player.hp > 0 and sum!=4:
        print(f"this room it`s empty it`s just the graveyard of {ear_plucker.name}")
        print(f"do you want to go to 'north' or to 'west'\n")
        text=input(" choose 'north' or 'west':  ")
        if text=="north":
            loc=3
        elif text=="west":
            loc=8
        else:
            pass


    elif loc==8 and player.hp > 0 and sum!=4:
        print("There are many plants in this place, it`s not easy to see.")
        print("You can choose to 'look' around, go to 'west','north' or go to 'east'\n")
        text=input("'look', 'west','north' or 'east': ")
        if text=="look" and player.hp > 0:
            print("you touched one of the plants and you got hurt... you lost 30Hp \n")
            Hero.poison(player)
            print(f"your hp level is {player.hp}")
            if player.hp<=0:
                break
        elif text=="west":
            loc=6
        elif text=="north":
            loc=5
        elif text=="east":
            loc=7
        elif player.hp<=0:
            break
        else:
            pass

    elif sum==4:
        break


if player.hp <=0:
    print("Game over.")

elif (angelus.alive_check()==False and bisontus.alive_check()==False 
                      and ear_plucker.alive_check()==False and the_driller.alive_check()==False):
    
    print(" Congratulations you beat all the oponents in the field but now you have your last oponent.")
    print(f"You have in front of you the powerful {Final_oponent.name} and his {Wolves_oponent.name}")
    print("There is no way out you have to fight until one wins")

    while player.hp>0 and Wolves_oponent.hp>0:
    #print(f"your hp level is {player.hp}")
   # print(f"The {Wolves_oponent.name} hp is {Wolves_oponent.hp}")
        if Wolves_oponent.hp>0 and player.hp>0:
            fight_wolves=Wolves_oponent.attack()
            if fight_wolves==True and player.hp>0:
                player.battle_run_wolves(Wolves_oponent)
                print(f"your hp level is {player.hp}")
                print(f"The wolves hp is {Wolves_oponent.hp}")
            elif fight_wolves==False and player.hp>0:
                player.battle(Wolves_oponent)
                print(f"your hp level is {player.hp}")
                print(f"The wolves hp is {Wolves_oponent.hp}")
            #Wolves_oponent.alive_check()

        elif Wolves_oponent.hp<=0:
            print(f"Congratulations you beat {Wolves_oponent.name}")
            print(f"Now it`s turn for {Final_oponent.name}")
            break
        elif player.hp<=0:
            break

    if Wolves_oponent.hp<=0:
        print(f"Congratulations you beat {Wolves_oponent.name}")
        print(f"Now it`s turn for {Final_oponent.name}")

    while player.hp>0 and Final_oponent.hp>0 and Wolves_oponent.hp<=0:
        #print(f"your hp level is {player.hp}")
        #print(f"The {Final_oponent.name} hp is {Final_oponent.hp}")
        if Final_oponent.hp>0 and player.hp>0:
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
        elif Final_oponent.hp<=0:
            break

        elif player.hp<=0:
            break

    if player.hp<=0:
        print("Game over. You lost")

    else:
        print(f"Congratulations!!  {player.name} won the game")
    




        
        



    
