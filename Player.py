class Player:
    def guessHighOrLow(self, card):
        if card <= 7:
            return True
        else:
            return False
    def reset(self):
        pass

class BadPlayer:
    def guessHighOrLow(self, card):
        return False
    def reset(self):
        pass

class WorsePlayer:
    def guessHighOrLow(self, card):
        return card >= 7
    def reset(self):
        pass

class MemoryPlayer:
    def __init__(self, numCards):
        self.numCards = numCards
        self.reset()
    def reset(self):
        self.memoryList = []
        for outer in range(1, 5):
            for inner in range(1, 14):
                self.memoryList.append(inner)
    def guessHighOrLow(self, card):
        self.memoryList.remove(card)
        numHigher = 0
        numLower = 0
        for c in self.memoryList:
            if card > c:
                numLower += 1
            elif card == c:
                numLower += 1
                numHigher += 1
            else:
                numHigher += 1
        return numHigher > numLower
        
class WorstPlayerEver:
    def __init__(self):
        self.friend = MemoryPlayer(0)
    def reset(self):
        self.friend.reset()
    def guessHighOrLow(self, card):
        return not self.friend.guessHighOrLow(card)

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

def testPlayer():
    p = Player()
    assert(p.guessHighOrLow(10) == False)
    #assert(p.guessHighOrLow(11) == True)
    assert(p.guessHighOrLow(0) == True)
    assert(p.guessHighOrLow(1) == True)
    assert(p.guessHighOrLow(13) == False)
    assert(p.guessHighOrLow(14) == False)
    assert(p.guessHighOrLow(7) == True)
    assert(p.guessHighOrLow(6) == True)
    assert(p.guessHighOrLow(8) == False)

def testMemoryPlayer():
    p = MemoryPlayer(52)
    # Confirm reset() works
    assert(p.guessHighOrLow(2) == True)
    assert(p.guessHighOrLow(2) == True)
    assert(p.guessHighOrLow(2) == True)
    assert(p.guessHighOrLow(2) == True)
    gotExcept = False
    try:
        p.guessHighOrLow(2)
    except:
        gotExcept = True
    assert(gotExcept)

    # Resetting should allow us to get a 2 again; clean deck
    p.reset()
    for suit in range(0, 4):
        assert(p.guessHighOrLow(1) == True)
        assert(p.guessHighOrLow(2) == True)
        assert(p.guessHighOrLow(3) == True)
        assert(p.guessHighOrLow(4) == True)
        assert(p.guessHighOrLow(5) == True)
    assert(p.guessHighOrLow(8) == True)
    assert(p.guessHighOrLow(11) == False)


def testCardCounter():
    p = CardCounter()
    # Test that the pivot shifts slightly around 7 when giving cards low then high
    assert(p.guessHighOrLow(4) == True)
    assert(p.guessHighOrLow(7) == True)
    assert(p.guessHighOrLow(12) == False)
    assert(p.guessHighOrLow(11) == False)
    assert(p.guessHighOrLow(11) == False)
    assert(p.guessHighOrLow(7) == False)

    # Verify if we front-load with low numbers, that high number guesses are different than default player
    p.reset()
    for k in range(0, 12):
        assert(p.guessHighOrLow(1 + (k % 3)) == True)
    # Our pivot point is exactly 10; shift it one more over, then test 10
    assert(p.guessHighOrLow(8) == True)
    assert(p.guessHighOrLow(10) == True)

if __name__ == "__main__":
    # testPlayer()
    #testMemoryPlayer()
    testCardCounter()
    print("Done")
