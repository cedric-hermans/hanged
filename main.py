import random

words = ["test", "python", "hangman"]

class Game:
    def __init__(self, word):
        self.word = word
        self.displayWord = ""
        self.guessedCharacters = []
        self.guessCount = 0
        self.isRunning = True

    def guess_character(self, guess):
        count = 0
        for i in enumerate(self.word):
            if i[1] == guess:
                count += 1
                self.displayWord = self.displayWord[0:i[0]] + guess + self.displayWord[i[0] + 1:]
        if count == 1:
            print("You got" , count, "right character")
        elif count > 1:
            print("You got", count, "right characters")
        else:
            self.guessedCharacters.append(guess)
            print("You guessed wrong")
            print("Guessed characters", self.guessedCharacters)

print("""Welcome to Hanged!
******************""")

game = Game(random.choice(words))
print("We got a word ready for you")
game.displayWord = game.word.replace(game.word, "_"*len(game.word))
print(game.displayWord)

while game.guessCount <= 7:
    print("Guess a letter:")
    player_guess = input()
    game.guess_character(player_guess)
    print(game.displayWord)


