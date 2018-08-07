import arcade
import random

class Bokstav:
    def __init__(self, bokstav, x, y):
        self.bokstav = bokstav
        self.x = x
        self.y = y

class MittSpel(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Bokstavsspel")
        arcade.set_background_color(arcade.color.WHITE)
        self.score = 0
        self.letters = []

    def update(self, delta_time):
        if random.random() > 0.96:
            self.letters.append(Bokstav(random.choice("abcdefghijklmnopqrstuvwxyz"), random.randint(50,750), 600))
        
        for bokstav in self.letters: 
            bokstav.y -= 1
            if bokstav.y < 0: 
                print("Du förlorade med bokstav", bokstav.bokstav, ". Game over!")
                exit()

    def on_draw(self):
        arcade.start_render()
        
        # Utritningskod
        for bokstav in self.letters: 
            arcade.draw_text(bokstav.bokstav, bokstav.x, bokstav.y, arcade.color.ARMY_GREEN, 20)
        arcade.draw_text("Poäng: " + str(self.score), 30, 550, arcade.color.AUBURN, 40)
        #arcade.finish_render() # Optional

    def on_key_press(self, key, modifier):
        for bokstav in self.letters: 
            if key == ord(bokstav.bokstav):
                self.score += 1
                self.letters.remove(bokstav)
MittSpel()
arcade.run()


