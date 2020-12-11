import math

# Player that knows a certain number of cards in memory.  Each time a
# card is dealt to the player, it remembers that card, and forgets all
# cards it knew that are older than a given threshold.  That threshold
# is provided at construction and represents the size of the memory.
class MemoryPlayer:
    # Create a memory with a given number of cards of memory
    def __init__(self, cardMemory):
        self.cardMemory = cardMemory
        self.reset()

    # Prepare the player for a new game
    def reset(self):
        self.cardsRemembered = []
        self.allRemainingCards = []
        for outer in range(1, 5):
            for inner in range(1, 14):
                self.allRemainingCards.append(inner)

    # Deal the card to the player, requesting high or low
    def guessHighOrLow(self, card):
        # Step 1: Guess
        numLower = (card - 1) * 4
        numHigher = (13 - card) * 4

        for memoryCard in self.cardsRemembered:
            if card > memoryCard:
                numLower -= 1
            elif card < memoryCard:
                numHigher -= 1

        guess = True if numHigher > numLower else False

        # Step 2: Remember incoming card
        self.cardsRemembered.append(card)
        if len(self.cardsRemembered) > self.cardMemory:
            self.cardsRemembered.pop(0)

        return guess

# Player that implements the Card Counting strategy.  It uses a pivot point
# around 7.0, and moves that up and down based on the incoming cards, by
# a factor of 0.125.  This was determined through trial and error.  This
# player attempts to approximate the card remembering, without actually
# remembering any cards.        
class CardCounter:
    def __init__(self):
        self.pivotPoint = 7

    # Deal the card to the player, adjusting the future pivot point
    def guessHighOrLow(self, card):
        returnValue = (card <= self.pivotPoint)

        # Add or subtract from the count based on the card being drawn
        # Change the pivot point
        if card > self.pivotPoint:
            self.pivotPoint -= 0.125
        elif card < self.pivotPoint:
            self.pivotPoint += 0.125

        return returnValue

    # Prepare the player for a new game
    def reset(self):
        self.pivotPoint = 7
