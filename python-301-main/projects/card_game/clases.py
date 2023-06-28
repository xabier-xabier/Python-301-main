
#class Card:
    #list_figures={"gold","cups","sword","club"}
    #list_values={1,2,3,4,5,6,7,8,9,"knave","knight","king"}

import random

class Carta:
    listaFiguras = ["Gold", "Cups", "Sword",
    "Club"]
    listaValores = ["narf", "1", "2", "3", "4", "5", "6",
    "7","8", "9", "10", "Knave", "Knight", "King"]

    def __init__(self, figura=0, valor=0):
        self.figura = figura
        self.valor = valor

    def __str__(self):
        return (self.listaValores[self.valor] + " " +
        self.listaFiguras[self.figura])

class Mazo:
    def __init__(self):
        self.cartas = []
        for figura in range(4):
           for valor in range(1, 14):
                self.cartas.append(Carta(figura, valor))

    def __str__(self):
        s = ""
        for i in range(len(self.cartas)):
            s = s+ str(self.cartas[i]) + "\n"
        return s
    
    
    def barajar(self):
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

    def repartir_3(self):
        out=[]
        count=0
        while count<3:
            out.append(self.cartas[count])
            count+=1
        self.cartas.remove(self.cartas[2])
        self.cartas.remove(self.cartas[1])
        self.cartas.remove(self.cartas[0])
        return out
    
    def show_card(self):
        out=[]
        out.append(self.cartas[0])
        self.cartas.remove(self.cartas[0])
        return out
    
    def remove_card(self):
        self.cartas.remove(self.cartas[0])

    #def delete_number(self,card):


class Player(Mazo):

    def __init__(self,*args):
        super().__init__()
        self.player_cards=args



    def remove_card(self,text):
        count=0
        for i in self.player_cards[0]:
            if i==text:
                self.player_cards[0].remove(self.player_cards[0][count])
            count+=1

    def __str__(self):
        for i in self.player_cards:
            print(i)
        return super().__str__()
    
    def add_card(self):
        self.player_cards[0].append(self.cartas[0])

    def check_figure(self):
        figure=None
        if "Gold" in self.player_cards[0]:
            figure="Gold"
        elif "Cups" in self.player_cards[0]:
            figure="Cups"
        elif "Sword" in self.player_cards[0]:
            figure="Sword"
        else:
            figure="Club"
        return figure
    
    def sum_cards(self,figure):
        sum=0
        if figure in self.player_cards[0]:
            if "3"+figure in self.player_cards[0]:
                sum+=10
            elif "7"+figure in self.player_cards[0]:
                sum+=5
            elif "1"+figure in self.player_cards[0]:
                sum+=5
            elif "2"+figure in self.player_cards[0]:
                sum+=5
            elif "4"+figure in self.player_cards[0]:
                sum+=5
            elif "5"+figure in self.player_cards[0]:
                sum+=5
            elif "6"+figure in self.player_cards[0]:
                sum+=5
            elif "8"+figure in self.player_cards[0]:
                sum+=5
            elif "9"+figure in self.player_cards[0]:
                sum+=5
            elif "10"+figure in self.player_cards[0]:
                sum+=5
            elif "Knave"+figure in self.player_cards[0]:
                sum+=5
            elif "Knight"+figure in self.player_cards[0]:
                sum+=5
            elif "King"+figure in self.player_cards[0]:
                sum+=5
            else:
                pass
        return sum


    
if __name__=="__main__":
    r1=Mazo()
    #print(r1.cartas[3])
    #r1.barajar
    #print(r1.barajar)
    r1.barajar()
    #print(r1)
    #r1.cartas.remove(r1.cartas[0])
    #print(r1)
    r2=r1.repartir_3()
    print(r2[0],r2[1],r2[2])

    #player_list=[1,2,3]
    #player_list[0]=r2[0]
    #player_list[1]=r2[1]
    #player_list[2]="10 Cups"

    #print(player_list)

    #r2[2]="3 Cups"
    #jugador=Player(player_list)
    jugador=Player(r2)                # Esta opcion es valida
    #jugador.remove_card('10 Cups')
    #print(jugador.player_cards[0][0])

    #if "Cups" in jugador.player_cards[0][2]:
        #print("its there")

    deck=r1.show_card()
    print(deck[0])

    #jugador.add_card()
    print(jugador.player_cards[0][0],jugador.player_cards[0][1],jugador.player_cards[0][2])

    player_deck=Player(deck)

    print(player_deck.player_cards[0][0])

    figure=player_deck.check_figure()  # hasta aqui esta bien

    #jugador.sum_cards(figure)

    print(jugador.sum_cards(figure))
    
    print(type(jugador.player_cards[0][0]))

   


    

    


    


