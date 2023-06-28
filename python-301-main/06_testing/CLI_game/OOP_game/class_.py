from random import randint

class Hero:

    def __init__(self,name,main_strength,hp):
        self.name=name
        self.main_strength=main_strength
        self.hp=hp
        pass

    def battle(self,other):
        hero_num=randint(1,6)
        opo_number=randint(1,6)
        if hero_num > opo_number:
            print(f"The hero {self.name} wins the battle\n")
            other.hp-=40
        elif hero_num < opo_number:
            print(f"The hero {self.name} lost the battle. You lose 10hp\n")
            self.hp-=10
        else:
            print("It`s a draw both lose 10hp\n")
            self.hp-=10
            other.hp-=10

    def feed(self):
        self.hp+=20
        pass

    def poison(self):
        self.hp-=30
        pass

    def battle_super_attack(self,other):
        hero_num=randint(1,6)
        opo_number=randint(1,6)
        if hero_num > opo_number+1:
            print(f"The hero {self.name} wins the battle\n")
            other.hp-=40
        elif hero_num < opo_number:
            print(f"The hero {self.name} lost the battle. You lose 50hp\n")
            self.hp-=50
        else:
            print("It`s a draw, you lose 20hp\n")
            self.hp-=20
            other.hp-=10

    def battle_run_wolves(self,other):
        hero_num=randint(1,6)
        opo_number=randint(1,6)
        if hero_num > opo_number+1:
            print(f"The hero {self.name} wins the battle\n")
            other.hp-=30
        elif hero_num < opo_number:
            print(f"The hero {self.name} lost the battle. You lose 30hp\n")
            self.hp-=30
        else:
            print("It`s a draw, you lose 10hp\n")
            self.hp-=10
            other.hp-=10


class Oponent:

    def __init__(self,name,main_strength,hp):
        self.name=name
        self.main_strength=main_strength
        self.hp=hp
        pass

    def alive_check(self):
        if self.hp<=0:
            alive=False
        else:
            alive=True
        return alive
    
class Wolves(Oponent):

    def __init__(self, name, main_strength, hp,run):
        super().__init__(name, main_strength, hp)
        self.run=run

    def attack(self):
        attack=None
        run=randint(1,6)
        if run>3:
            attack=True
        else:
            attack=False
        return attack


class Final_Oponent(Oponent):

    def __init__(self, name, main_strength, hp,extra_hp):
        super().__init__(name, main_strength, hp)
        self.extra_hp=extra_hp

    def attack(self):
        super_attack=None
        self.extra_hp=randint(1,6)*4            # extra hp
        self.hp+=self.extra_hp
        if self.extra_hp+self.hp>115:
            super_attack=True
        else:
            super_attack=False

        return super_attack



