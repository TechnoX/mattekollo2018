import math
class komplex():
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def realdel(self):
        return self.re
    def imaginardel(self):
        return self.im
    def rect(self):
        return (self.re, self.im)
    def polar(self):
        return (self.arg(), abs(self))
    def __str__(self):
        return str(self.re) + " + " + str(self.im) + "i"

    def __add__(self, HL):
        return komplex(self.re + HL.re, self.im + HL.im)

    def __abs__(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

    def arg(self):
        return math.atan2(self.im, self.re)
    
    def is_real(self):
        return self.im == 0

ettTal = komplex(3,4)
ettAnnatTal = komplex(5,2)

print(ettTal + ettAnnatTal)
#ettTal += ettAnnatTal
ettAnnatTal += ettTal
print(abs(ettAnnatTal))
print((ettAnnatTal + komplex(0,-6)).is_real())


