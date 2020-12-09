class CardCounter:
    def __init__(self):
        self.pivotPoint = 7

    def guessHighOrLow(self, card):
        returnValue = (card <= self.pivotPoint)

        # Add or subtract from the count based on the card being drawn
        # Change the pivot point
        if card > self.pivotPoint:
            self.pivotPoint -= 0.25
        elif card < self.pivotPoint:
            self.pivotPoint += 0.25

        return returnValue

    def reset(self):
        self.pivotPoint = 7

def testCardCounter():
    p = CardCounter()
    # Test that the pivot shifts slightly around 7 when giving cards low then high
    assert(p.guessHighOrLow(4) == True)
    assert(p.guessHighOrLow(7) == True)
    assert(p.guessHighOrLow(12) == False)
    assert(p.guessHighOrLow(11) == False)
    assert(p.guessHighOrLow(11) == False)
    assert(p.guessHighOrLow(7) == False)
    p.reset()

    for k in range(0, 12):
        newCard = int(k / 4) + 10
        assert(p.guessHighOrLow(newCard) == False)
        #assert(p.guessHighOrLow(1 + (k % 3)) == True)
    assert(p.guessHighOrLow(7) == False)
    assert(p.guessHighOrLow(6) == False)
    assert(p.guessHighOrLow(5) == False)
    print("Done!")

testCardCounter()
