import random

words = ["test", "python", "hangman"]

class Game:
    def __init__(self, word):
        self.word = word
        self.displayWord = ""
        self.guessCount = 0
        self.isRunning = True

print("""Welcome to Hanged!
******************""")

game = Game(random.choice(words))
print("We got a word ready for you")
game.displayWord = game.word.replace(game.word, "_"*len(game.word))
print(game.displayWord)

while game.guessCount <= 7:
    print("Guess a letter:")
    guess = input()
    i = game.word.find(guess)
    if i == -1:
        print("Letter not found")
    else:
        print("Letter found")
        game.displayWord = game.displayWord[0:i] + guess + game.displayWord[i+1:]
        print(game.displayWord)


