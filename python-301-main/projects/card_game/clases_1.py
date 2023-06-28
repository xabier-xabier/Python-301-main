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
    
    def remove_card1(self):
        self.cartas.remove(self.cartas[0])



class Player(Mazo):

    def __init__(self,*args):
        super().__init__()
        self.player_cards=args



    def remove_card(self,text):
        if text in str(self.player_cards[0][0]):
            self.player_cards[0].remove(self.player_cards[0][0])
        elif text in str(self.player_cards[0][1]):
            self.player_cards[0].remove(self.player_cards[0][1])
        elif text in str(self.player_cards[0][2]):
            self.player_cards[0].remove(self.player_cards[0][2])
        else:
            pass
            


    def __str__(self):
        for i in self.player_cards:
            print(i)
        return super().__str__()
    
    def add_card(self):
        self.player_cards[0].append(self.cartas[0])

    def check_figure(self):
        figure=None
        if "Gold" in str(self.player_cards[0][0]):
            figure="Gold"
        elif "Cups" in str(self.player_cards[0][0]):
            figure="Cups"
        elif "Sword" in str(self.player_cards[0][0]):
            figure="Sword"
        else:
            figure="Club"
        return figure
    
    def sum_cards(self,figure):
        sum=0
        for i in range(0,3,1):
            if "3"+" "+figure == str(self.player_cards[0][i]):
                sum+=10
            elif "1"+" "+figure == str( self.player_cards[0][i]):
                sum+=11
            elif "Knave"+" "+figure == str(self.player_cards[0][i]):
                sum+=2
            elif "Knight"+" "+figure == str(self.player_cards[0][i]):
                sum+=3
            elif "King"+" "+figure == str(self.player_cards[0][i]):
                sum+=4
            else:
                pass
        return sum
    

if __name__=="__main__":
    r1=Mazo()
    r1.barajar()
    r2=r1.repartir_3()
    print(r2[0],r2[1],r2[2])

    #text=input("selecciona una carta")

    #if text==str(r2[0]):
        #print("yes")
    #elif text==str(r2[1]):
        #print("yes")
    #elif text==str(r2[2]):
        #print("yes")

    jugador=Player(r2)
    deck=r1.show_card()
    print(jugador.player_cards[0][0],jugador.player_cards[0][1],jugador.player_cards[0][2])
    #text=input("Que carta quieres descartar? ")
    #jugador.remove_card(text)
    #print(jugador.player_cards[0])
    #print(jugador.player_cards[0][0],jugador.player_cards[0][1])
    #jugador.add_card()
    #print(jugador.player_cards[0][0],jugador.player_cards[0][1],jugador.player_cards[0][2])
    deck=r1.show_card()
    print(deck[0])
    player_deck=Player(deck)
    print(player_deck.player_cards[0][0])    
    figure=player_deck.check_figure()
    print(figure)
    print(jugador.sum_cards((figure)))