import arcade
import random
class Bokstav:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y
    def update(self):
        self.y -= 2
    
class MittSpel(arcade.Window):
    def __init__(self, bredd, hojd):
        super().__init__(bredd, hojd, "Spel")
        arcade.set_background_color(arcade.color.AMAZON)
        self.letters = []
        self.score = 0
        self.game_over = False
        
    def on_draw(self):
        arcade.start_render()

        for letter in self.letters:
            arcade.draw_text(letter.letter, letter.x, letter.y, arcade.color.ARMY_GREEN, 20)
        arcade.draw_text("Poäng: " + str(self.score), 30, 550, arcade.color.AUBURN, 30)
        
    def update(self, delta_time):
        if self.game_over:
            return
        if random.random() > 0.9:
            self.letters.append(Bokstav(random.choice("abcdefghijklmnopqrstuvwxyz"), random.randint(50,750), 600))
            
        for letter in self.letters:
            letter.update()
            if letter.y < 20:
                print("Lost letter ", letter.letter, ". Game Over!")
                self.game_over = True

    def on_key_press(self, key, modifier):
        if self.game_over:
            return
        for letter in self.letters:
            if ord(letter.letter) == key:
                self.letters.remove(letter)
                self.score += 1
        
game = MittSpel(800, 600)

arcade.run()
