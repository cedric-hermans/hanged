class Game:
    def __init__(self, word):
        self.word = word
        self.guessCount = 0
        self.isRunning = True

print("""Welcome to Hanged!
------------------
Press [S]tart to begin a new game""")
game = Game("test")
