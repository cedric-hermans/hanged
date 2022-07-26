import game
import requests
import json

request = requests.get("https://random-words-api.vercel.app/word")
json_data = request.json()
word = json_data[0]["word"].lower()

print("""Welcome to Hanged!
******************""")

game = game.Game(word)
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


