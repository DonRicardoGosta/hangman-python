import os, sys

if __name__ == "__main__":
    new_game = Game('kiskacsa',6)
    new_game.play()

class Game:

    usedLetters=[]
    hidedWord =""
    run=True

    def __init__(self, word, lives):
        self.word = word.lower()
        self.lives = lives
        self.hide_characters()

    def play(self):
        pass

    def is_num(self,str):
        pass

    def hide_characters(self):
        pass

    def reveal_characters(self,userG):
        pass
    def printGameState(self):
        pass

    def printWithDelay(self,message):
        pass

    def ask_for_a_letter(self, hidedWord):
        pass