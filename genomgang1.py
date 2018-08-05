class Fruit():
    color = "Osynlig"
    taste = "Äckliga"
    has_peel = False
    name = "Nothing"
    
    def __init__(self, name, taste, has_peel, color):
        self.color = color
        self.name = name
        self.taste = taste
        self.has_peel = has_peel
       
    def peel(self):
        if self.has_peel:
            print("Du skalade just en " + self.name)
        else:
            print("Hallå! Det går ju inte att skala en " + self.name)

    def __str__(self):
        return "Detta är en " + self.name + " som är " + self.taste



frukt = Fruit("Banan", "God", True, "Gul")

print(frukt.name)
print("Bananen är " + frukt.color)

jordgubbe = Fruit("Jordgubbe", "Söt", False, "Röd")


frukt.peel()
jordgubbe.peel()

print(jordgubbe)
print(frukt)



apple1 = Fruit("Äpple", "Sur", True, "Grön")
apple2 = Fruit("Äpple", "Mjölig", True, "Röd")
apple3 = Fruit("Äpple", "Sur", True, "Gul")


class Apple(Fruit):
    def __init__(self, color, taste): 
        super().__init__("Äpple", taste, True, color)
   
    def kasta(self):
        print("Du kastade sönder ett fönster!")


apple4 = Apple("Röd", "Mjölig")
print(apple4.name)
print(apple4)
apple4.peel()
apple4.kasta()


apple1.kasta()














