import arcade
import random # För slumptalsgenerator

class Tecken:
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y

class MittSpel(arcade.Window): 
    def __init__(self): 
        super().__init__(800, 600, "Bokstavsspel")
        arcade.set_background_color(arcade.color.WHITE)
        self.letters = [] # Lista över bokstäverna
        self.score = 0    # Nuvarande poäng

    def update(self, delta_time):
        if random.random() > 0.96:                               # 4% chans att skapa en bokstav
            letter = random.choice("abcdefghijklmnopqrstuvwxyz") # Väljer en slumpmässig bokstav av dessa 
            x_koordinat = random.randint(50, 750)                # Väljer en slumpmässig koordinat mellan 50 och 750
            y_koordinat = 600                                    # Sätter Y koordinaten till högst upp i fönstret
            tecken = Tecken(letter, x_koordinat, y_koordinat)    # Skapar ett objekt av typen Tecken
            self.letters.append(tecken)                          # Lägger till objektet i vår letters lista

        for tecken in self.letters:                              # Loopar igenom alla bokstäver som vi har i listan
            tecken.y -= 1                                        # Minskar dess y koordinat så den rör sig nedåt
            if tecken.y < 20:                                    # Om bokstaven är längst ned har man förlorat
                print("Lost on letter", tecken.letter, ". Game Over!")
                exit()

    def on_draw(self):
        arcade.start_render()

        for tecken in self.letters:                              # Går igenom alla bokstäver och ritar ut dem
            arcade.draw_text(tecken.letter, tecken.x, tecken.y, arcade.color.ARMY_GREEN, 20)
        
        # Skriver ut vår nuvarande poäng
        arcade.draw_text("Poäng: " + str(self.score), 20, 540, arcade.color.ARMY_GREEN, 40)

    def on_key_press(self, key, modifier):
        # Går igenom alla våra bokstäver i listan
        for tecken in self.letters: 
            # Kollar om bokstaven matchar den tangent vi tryckt på.
            # ord() funktionen konverterar bokstaven till ASCII som är samma kod som arcade sparar i key variabeln
            if ord(tecken.letter) == key:
                self.letters.remove(tecken)    # Tar bort bokstaven från listan om den matchar villkoret i if-satsen ovan
                self.score += 1                # Ökar vår poäng med ett. 

game = MittSpel()
arcade.run()










