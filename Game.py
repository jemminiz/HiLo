"""
0: Prepare
   Create a game deck
   Create a player
1. Draw a card from deck, give to player
  2. Ask player higher or lower
  3. Draw a card from deck, give to player
  4. Give a point based on whether player was correct
  5. if card list is empty, then break out of loop (go to step 7)
  6. Else, Go to step 2
7. Calculate points and declare winner

0: Prepare:
   Create a game deck
   Create a player
1. Draw a card from deck
  2. Give card to player, ask player higher or lower
  3. Draw a card from deck
  4. Give a point based on whether player was correct
  5. if card list is empty, then break out of loop (go to step 7)
  6. Else, Go to step 2
7. Calculate points and declare winner

"""

import Deck

LOWER = False
HIGHER = True
class Player:
    def guessHighOrLow(self, card):
        if card < 7:
            return HIGHER
        else:
            return LOWER

class Game:
    def Reset(self):
        pass
    def Play(self):
        # 1. Draw a card from deck
        card = self.gameDeck.draw()

        while True:
            # 2. Give card to player, ask player higher or lower
            guess = self.player.guessHighOrLow(card)

            # 3. Draw a card from deck
            newCard = self.gameDeck.draw()
            #print(f"Got {newCard} compared vs old {card}")

            # 4. Give a point based on whether player was correct
            if newCard == card:
                self.numPoints += 1   # Player wins on tie
            elif guess == HIGHER and newCard > card:
                self.numPoints += 1   # It was higher, and player guessed right
            elif guess == LOWER and newCard < card:
                self.numPoints += 1   # It was lower, and player guessed right

            card = newCard
            # 5. if card list is empty, then break out of loop (go to step 7)
            if self.gameDeck.empty():
                break
            # 6. Else, Go to step 2
    def NumWins(self):
        return self.numPoints
    def __init__(self):
        # Prepare
        self.gameDeck = Deck.Deck()
        self.player = Player()
        self.numPoints = 0





numPoints = 0
numGames = 0
for k in range(0,5):
    newGame = Game()
    newGame.Play()
    numPoints += newGame.NumWins()
    numGames += 1

# 7. Calculate points and declare winner
#print("Num points: " + str(newGame.NumWins()))
print("Num points: " + str(numPoints))
print("Average points: " + str(numPoints/numGames))


