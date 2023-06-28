
import random
cartas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

nCartas = 5
for i in range(nCartas):
    j = random.randrange(i, nCartas)
    cartas[i], cartas[j] = cartas[j], cartas[i]

print(cartas)