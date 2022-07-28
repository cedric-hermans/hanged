import game
import requests
import json

print("""Welcome to Hanged!
******************""")

request = requests.get("https://random-words-api.vercel.app/word")
json_data = request.json()
word = json_data[0]["word"].lower()
game = game.Game(word)
print("We got a word ready for you")
game.display_word = game.word.replace(game.word, "_"*len(game.word))
print(game.display_word)

while game.guess_count < 7 and game.is_running:
    print("Guess a letter:")
    player_guess = input()
    if player_guess not in game.guessed_characters\
            and len(player_guess) == 1\
            and player_guess.isdigit() == False:
        game.guess_character(player_guess)
    else:
        print("Incorrect guess!")

if game.guess_count < 7:
    print("You won!")
else:
    print("Alas, you got hanged..")
    print("The word was", game.word)

print("You scored", game.score, "points")


