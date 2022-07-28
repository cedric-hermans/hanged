class Game:
    def __init__(self, word):
        self.word = word
        self.display_word = ""
        self.guessed_characters = []
        self.guess_count = 0
        self.score = 0
        self.is_running = True

    def guess_character(self, guess):
        hit = False
        for i in enumerate(self.word):
            if i[1] == guess:
                hit = True
                self.score += 20
                self.display_word = self.display_word[0:i[0]] + guess + self.display_word[i[0] + 1:]
        if hit is False:
            self.guess_count += 1
            self.score -= 10
            self.guessed_characters.append(guess)
            print("You guessed wrong")

        print(self.draw_sequence(self.guess_count))
        print("Guessed characters", self.guessed_characters)

        self.check_for_win()
        print(self.display_word)

    def check_for_win(self):
        if self.display_word == self.word:
            self.is_running = False
            if self.guess_count == 0:
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