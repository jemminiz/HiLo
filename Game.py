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
import Player
import random

LOWER = False
HIGHER = True


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
    def __init__(self, player):
        # Prepare
        self.gameDeck = Deck.Deck()
        self.player = player
        self.numPoints = 0

import statistics
import math

allStdDevs = []
def runExperiments(label, thisPlayer):
    numPoints = 0
    numGames = 0
    allPoints = []
    random.seed(12)

    for k in range(0,1000):
        newGame = Game(thisPlayer)
        newGame.Play()
        numPoints += newGame.NumWins()
        allPoints.append(newGame.NumWins())
        numGames += 1
        thisPlayer.reset()

    # 7. Calculate points and declare winner
    mean = numPoints/numGames
    stddev = statistics.stdev(allPoints)
    allStdDevs.append(stddev)
    print(label + "\t" + str(mean)  + "\t" + str(stddev))

for cards in range(0, 52, 5):
    runExperiments(f"Memory {cards}", Player.MemoryPlayer(cards))

totalStdDev = statistics.stdev(allStdDevs)
totalMean = statistics.mean(allStdDevs)
print(f"Std Dev Report:")
print(f"Mean: {totalMean}")
print(f"Std Dev: {totalStdDev}")

runExperiments("Card Counter", Player.CardCounter())


