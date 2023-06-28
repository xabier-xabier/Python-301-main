from clases_1 import Carta,Mazo,Player


print(""" 
                    Welcome to the simple version of "La Brisca" Spanish card game.
                    You will be given 3 random cards and your oponent another 3 cards.
                    Then the deck will show one card in the middle. 
                    There is a total of 52 cards divided in 4 blocks (4 figures) and 13 cards per figure.
                    Figures =(Gold, Cups, Swords and Club)
                    Cards per figure =(1,2,3,4,5,6,7,8,9,10,Knave,Knight,King)
                    
                    The card shown by the deck will decide which Figure will count to sum points, 
                    only the cards belonging to that figure will count.
                    1= 11 points, 3= 10 points, King= 4 points, Knight= 3 points, Knave=2 points
                    """)

count=0

r1=Mazo()

r1.barajar()

r2=r1.repartir_3()
r3=r1.repartir_3()
jugador=Player(r2)
computer=Player(r3)
deck=r1.show_card()


print("The 3 cards you got from the deck are:")
print(jugador.player_cards[0][0])
print(jugador.player_cards[0][1])
print(jugador.player_cards[0][2])
print("\n")
print("The card that will determine which figure counts it`s shown below")
print(deck[0])
#print("You can choose to discard up to 2 cards or keep the cards you got.")
#text=input("choose 'keep' or 'discard': ")
text=None
while count<2 or text=="keep":
    print("You can choose to discard up to 2 cards or keep the cards you got.")
    text=input("choose 'keep' or 'discard': ")
    if text=="discard":

        text=input("please write the card you want to discard: ")
        jugador.remove_card(text)
        jugador.add_card()
        r1.remove_card1()
        count+=1
        print("Your cards right now are")
        print(jugador.player_cards[0][0])
        print(jugador.player_cards[0][1])
        print(jugador.player_cards[0][2])
    elif text=="keep":
        break

player_deck=Player(deck)
figure=player_deck.check_figure()


if jugador.sum_cards(figure)>computer.sum_cards(figure):
    print("Congratulations!! You won the game ")
    print(f"Your score was {jugador.sum_cards(figure)} and the score of your oponent was {computer.sum_cards(figure)}")
    print(f"""The cards of your opoenent were:
                {computer.player_cards[0][0]}
                {computer.player_cards[0][1]}
                {computer.player_cards[0][2]}""")

elif jugador.sum_cards(figure)<computer.sum_cards(figure):
    print("You lost the game....")
    print(f"Your score was {jugador.sum_cards(figure)} and the score of your oponent was {computer.sum_cards(figure)}")
    print(f"""The cards of your opoenent were:
                {computer.player_cards[0][0]}
                {computer.player_cards[0][1]}
                {computer.player_cards[0][2]}""")

else:
    print("It`s a draw.")
    print(f"Your score was {jugador.sum_cards(figure)} and the score of your oponent was {computer.sum_cards(figure)}")
    print(f"""The cards of your opoenent were:
                {computer.player_cards[0][0]}
                {computer.player_cards[0][1]}
                {computer.player_cards[0][2]}""")

