import math

class Komplex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def rektangular_form(self):
        return (self.re, self.im)

    def __str__(self):
        return str(self.re) + " + " + str(self.im) + "i"
    
    def __add__(self, HL):
        return Komplex(self.re + HL.re, self.im + HL.im)

    def __abs__(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def is_real(self):
        return self.im == 0


ettTal = Komplex(4,1)
print(ettTal.is_real())

ettAnnatTal = Komplex(2,7)
print(ettTal + ettAnnatTal)

ettTal += 6

print(abs(ettTal))






















