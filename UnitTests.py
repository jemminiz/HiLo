import Deck
import Player

def deckTests():
    gameDeck = Deck.Deck()
    gameDeck.printCard()
    gameDeck.draw()
    gameDeck.printCard()
    print(gameDeck.empty())
    gameDeck.printCard()

def testMemoryPlayer():
    p = Player.MemoryPlayer(52)
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

def testCardCounter2():
    p = Player.CardCounter()
    assert(p.guessHighOrLow(3) == True)
    assert(p.guessHighOrLow(10) == False)
    assert(p.guessHighOrLow(2) == True)
    assert(p.guessHighOrLow(5) == True)
    assert(p.guessHighOrLow(1) == True)
    assert(p.guessHighOrLow(7) == True)

def testCardCounter():
    p = Player.CardCounter()
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

def testFaultyMemory():
    p = Player.MemoryPlayer(15)
    p.guessHighOrLow(1)
    p.guessHighOrLow(1)
    p.guessHighOrLow(1)
    p.guessHighOrLow(1)
    p.guessHighOrLow(2)
    p.guessHighOrLow(3)
    p.guessHighOrLow(3)
    p.guessHighOrLow(3)
    p.guessHighOrLow(3)
    p.guessHighOrLow(4)
    p.guessHighOrLow(8)

def testCardCounter3():
    p = Player.CardCounter()
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
    # Pivot moves 12 times, by 0.125, or (7 - 1.5) == 5.5
    assert(p.guessHighOrLow(7) == False)
    # Pivot is up to 5.625
    assert(p.guessHighOrLow(6) == False)
    # Pivot is up to 5.75
    assert(p.guessHighOrLow(5) == True)

deckTests()
#testPlayer()
#testMemoryPlayer()
#testCardCounter()
#testFaultyMemory()
testCardCounter2()
testCardCounter3()
print("Done!")
