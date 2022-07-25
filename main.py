import requests
import json

request = requests.get("https://random-words-api.vercel.app/word")
json_data = request.json()
word = json_data[0]["word"].lower()

class Game:
    def __init__(self, word):
        self.word = word
        self.displayWord = ""
        self.guessedCharacters = []
        self.guessCount = 0
        self.score = 0
        self.is_running = True

    def guess_character(self, guess):
        count = 0
        for i in enumerate(self.word):
            if i[1] == guess:
                count += 1
                self.score += 20
                self.displayWord = self.displayWord[0:i[0]] + guess + self.displayWord[i[0] + 1:]
        if count == 1:
            print("You got" , count, "right character")
        elif count > 1:
            print("You got", count, "right characters")
        else:
            self.guessCount+=1
            self.score -= 10
            self.guessedCharacters.append(guess)
            print("You guessed wrong")

        print(self.draw_sequence(self.guessCount))
        print("Guessed characters", self.guessedCharacters)

        self.check_for_win()
        print(self.displayWord)

    def check_for_win(self):
        if self.displayWord == self.word:
            self.is_running = False
            if self.guessCount == 0:
                self.score += 100

    def draw_sequence(self, count):
        match count:
            case 0:
                return ""
            case 1:
                return """ 
 
 
 
 
 
/ \\ """
            case 2:
                return """ 
 |        
 |       
 |      
 |      
 |
/ \\ """
            case 3:
                return """ ----------
 |        
 |       
 |      
 |       
 |
/ \\ """
            case 4:
                return """ ----------
 |        |
 |        
 |       
 |     
 |
/ \\ """
            case 5:
                return """ ----------
 |        |
 |        0
 |       
 |      
 |
/ \\ """
            case 6:
                return """ ----------
 |        |
 |        0
 |       /|\\
 |       
 |
/ \\ """
            case 7:
                return """ ----------
 |        |
 |        0
 |       /|\\
 |       / \\
 |
/ \\ """

print("""Welcome to Hanged!
******************""")

game = Game(word)
print("We got a word ready for you")
game.displayWord = game.word.replace(game.word, "_"*len(game.word))
print(game.displayWord)

while game.guessCount < 7 and game.is_running:
    print("Guess a letter:")
    player_guess = input()
    if player_guess not in game.guessedCharacters\
            and len(player_guess) == 1\
            and player_guess.isdigit() == False:
        game.guess_character(player_guess)
    else:
        print("Incorrect guess!")


if game.guessCount < 7:
    print("You won!")
else:
    print("Alas, you got hanged..")
    print("The word was", game.word)

print("You scored", game.score, "points")


