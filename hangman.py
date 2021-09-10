import os, sys
from art import tprint
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Game:

    usedLetters=[]
    hidedWord =""
    run=True

    def __init__(self, word, lives):
        self.word = word.lower()
        self.lives = lives
        self.hide_characters()

    def play(self):
        while(self.run):
            self.ask_for_a_letter(self.hidedWord)

    def is_num(self,str):
        try:
            return int(str)
        except ValueError:
            return None

    def hide_characters(self):
        for underscore in self.word:
            self.hidedWord += "_"

    def reveal_characters(self,userG):
        wrongG = True
        for index in range(len(self.word)):
            if self.word[index] == userG:
                yourStringNew="".join((self.hidedWord[:index],userG,self.hidedWord[index+1:]))
                self.hidedWord = yourStringNew
                wrongG = False

        if wrongG:
            self.printWithDelay("This time you were wrong, you lost 1 live(Hit enter)")
            self.lives-=1
            if self.lives == 0:
                clearConsole()
                print("You ran out of lives")
                tprint("you lost")
                sys.exit()

    def printGameState(self):
        clearConsole()
        tprint("Hangman")
        print("Your lives: ", self.lives,"\n\nUsed Letters: ",*self.usedLetters,"\n\n")
        printVariable="\t\t\t"
        for underscore in self.hidedWord:
            printVariable+=underscore+" "
        print(printVariable)
        print("\n\n\n\t\tPlease guess a letter or type 'exit': \n")

    def printWithDelay(self,message):
        input(message)

    def ask_for_a_letter(self, hidedWord):
        while(self.run):
            self.printGameState()
            if "_" in self.hidedWord:
                userIn = input("\t\t\t\t").lower()
                if(self.is_num(userIn)!=None):
                    self.printWithDelay("You wrote a numbert not a letter, please try again(Hit enter).")
                elif userIn =="":
                    self.printWithDelay("You hit enter and did not write anything, please try again(Hit enter).")
                elif len(userIn) > 1:
                    if userIn == "exit":
                        sys.exit()
                    else:
                        self.printWithDelay("You wrote too many letters, please enter only one(Hit enter)")
                else:
                    if userIn in self.usedLetters:
                        self.printWithDelay("'{0}' is already used".format(userIn))
                    else:
                        self.usedLetters.append(userIn)
                        self.reveal_characters(userIn)
            else:
                self.run = False
        clearConsole()
        tprint("You won")
        sys.exit()

if __name__ == "__main__":
    new_game = Game('kiskacsa',6)
    new_game.play()
    