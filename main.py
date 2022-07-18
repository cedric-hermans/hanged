import random

words = ["test", "python", "hangman"]

class Game:
    def __init__(self, word):
        self.word = word
        self.guessCount = 0
        self.isRunning = True

print("""Welcome to Hanged!
******************""")

game = Game(random.choice(words))
print("We got a word ready for you")
print(game.word.replace(game.word, "_"*len(game.word)))


