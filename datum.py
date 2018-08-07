from datetime import date

a = int(input("Del 1: "))
b = int(input("Del 2: "))
c = int(input("Del 3: "))

datum = []
try:
    datum.append(date(2000+a,b,c))
except:
    pass
try:
    datum.append(date(2000+a,c,b))
except:
    pass
try:
    datum.append(date(2000+b,a,c))
except:
    pass
try:
    datum.append(date(2000+b,c,a))
except:
    pass
try:
    datum.append(date(2000+c,a,b))
except:
    pass
try:
    datum.append(date(2000+c,b,a))
except:
    pass

minsta = min(datum)
print("Year: "+ str(minsta.year) + ", Month: " + str(minsta.month) + ", Day: " + str(minsta.day))
