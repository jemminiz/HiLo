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

# Prepare
gameDeck = Deck.Deck()
player = Player()
numPoints = 0
# 1. Draw a card from deck
card = gameDeck.draw()

while True:
    # 2. Give card to player, ask player higher or lower
    guess = player.guessHighOrLow(card)

    # 3. Draw a card from deck
    newCard = gameDeck.draw()
    print(f"Got {newCard} compared vs old {card}")

    # 4. Give a point based on whether player was correct
    if newCard == card:
        numPoints += 1   # Player wins on tie
    elif guess == HIGHER and newCard > card:
        numPoints += 1   # It was higher, and player guessed right
    elif guess == LOWER and newCard < card:
        numPoints += 1   # It was lower, and player guessed right

    card = newCard
    # 5. if card list is empty, then break out of loop (go to step 7)
    if gameDeck.empty():
        break
    # 6. Else, Go to step 2

# 7. Calculate points and declare winner
print("Num points: " + str(numPoints))
