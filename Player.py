class Player:
    def guessHighOrLow(self, card):
        if card <= 7:
            return True
        else:
            return False

if __name__ == "__main__":
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
    print("Done")
