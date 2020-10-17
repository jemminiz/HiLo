import random

class Deck:
    def __init__(self):
        self.cardlist = []
        for outer in range(1, 5):
            for inner in range(1, 14):
                self.cardlist.append(inner)
        self.shuffle()
    
    def printCard(self):
        print(self.cardlist)

    def draw(self):
        return self.cardlist.pop()

    def shuffle(self):
        random.shuffle(self.cardlist)

    def empty(self):
        if len(self.cardlist) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    gameDeck = Deck()
    gameDeck.printCard()
    gameDeck.draw()
    gameDeck.printCard()
    print(gameDeck.empty())
    ##gameDeck.shuffle()
    ##gameDeck.printCard()
