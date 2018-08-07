

summa = 0
for i in range(n):
    summa += i

print(summa)


-------------------------------------------------------------------





for i in range(n):
    for j in range(n):
        print(i,j)


-------------------------------------------------------------------



for i in range(n):
    for j in range(n):
        print(i,j)
        print(i,j)
        print(i,j)



-------------------------------------------------------------------



#Förbättra
summa = 0
for i in range(n):
    summa += i

print(summa)

#Svar
summa = ??

print(summa)


-------------------------------------------------------------------



import random

lista = []

for i in range(n):
    lista.append(random.random())

lista.sort()

print( lista )


_---------------------------------------


G = {
    'S' : [('A', 2)],
    'A' : [('S', 2), ('B', 3), ('C', 13) ],
    'B' : [('A', 3), ('C', 5) ],
    'C' : [('A', 13), ('B', 5), ('M', 8)],
    'M' : [('C', 8)]
}
