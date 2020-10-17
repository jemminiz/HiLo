import random

#class Deck

cardlist = []
for outer in range(1, 5):
    for inner in range(1, 14):
        cardlist.append(inner)



random.shuffle(cardlist)

#Shuffle
print(cardlist)

#Shuffle
random.shuffle(cardlist)
print(cardlist)

