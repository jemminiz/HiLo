import random

# Represents a shuffled card deck
class Deck:
    def __init__(self):
        self.cardlist = []
        for outer in range(1, 5):
            for inner in range(1, 14):
                self.cardlist.append(inner)
        self.shuffle()

    # Print all cards in the deck    
    def printCard(self):
        print(self.cardlist)

    # Removes top card from the deck
    def draw(self):
        return self.cardlist.pop()

    # Shuffles remaining cards
    def shuffle(self):
        random.shuffle(self.cardlist)

    # Returns true if the deck has no cards
    def empty(self):
        return len(self.cardlist) == 0
