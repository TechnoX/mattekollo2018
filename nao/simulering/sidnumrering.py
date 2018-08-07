

sidor = input("Antal sidor ? ")
antal = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in range(1, int(sidor)+1, 2):
    for l in str(i):
        antal[l]+=1

for i in antal:
    print(str(antal[i]) + " ",end="")

