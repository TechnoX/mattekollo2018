#!/usr/bin/python
# -*- coding: utf-8 -*-
class Fruit:
    def __init__(self, kind, color, taste, can_peel):
        self.kind = kind
        self.color = color
        self.taste = taste
        self.can_peel = can_peel


    def peel(self):
        if self.can_peel:
            print("Du skalade just en " + self.kind)
        else:
            print("Hallå! Du kan ju inte skala en " + self.kind)


    def __str__(self):
        return self.kind
    
banan = Fruit("Banan", "Gul", "God", True)
print("Bananen är " + banan.color)

jordgubbe = Fruit("Jordgubbe", "Röd", "Söt", False)

banan.peel()
jordgubbe.peel()




print(banan) # Lägg till __str__ efter detta!


apple1 = Fruit("Äpple", "Grönt", "Surt", True)
apple2 = Fruit("Äpple", "Rött", "Smuligt", True)


class Apple(Fruit):
    def __init__(self, color, taste):
        super().__init__("Äpple", color, taste, False)

apple3 = Apple("Grönt", "Gott")
print(apple3)
