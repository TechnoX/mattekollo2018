from time import sleep

with open("karta.txt", "r") as f: 
    line = f.readline().strip()
    start = line.split(",")
    start = [int(e) for e in start]
    line = f.readline().strip()     
    slut = line.split(",")
    slut = [int(e) for e in slut]
    resten = f.read()
    karta = resten.split('\n')
    karta = karta[:-1]

print(karta)

hojd = len(karta)
bredd = len(karta[0])

min_drag = 1000000

besokt = [[False for b in range(bredd)] for h in range(hojd)]
#besokt = [[False]*bredd for h in range(hojd)]


def visualisera():
    print(chr(27) + "[2J")
    for r in range(hojd):
        for k in range(bredd):
            if besokt[r][k]:
                print(chr(183),end='')
            else:
                print(karta[r][k], end='')
        print("")
    sleep(0.1)
    print("")


class Position:
    def __init__(self, r, k, drag):
        self.r = r
        self.k = k
        self.drag = drag

lista = [Position(start[0], start[1], 0)]


def add(r, k, drag):
    if karta[r][k] == "#": # Vi kan inte gå in i en vägg
        return
    if besokt[r][k]: # Redan besökt
        return

    pos = Position(r, k, drag) # Skapar position
    lista.insert(0, pos)       # Lägger till först i listan
    besokt[r][k] = True        # Markerar som besökt


while lista:
    # nuvarande position
    pos = lista.pop()
    visualisera()
    
    if pos.r == slut[0] and pos.k == slut[1]:
        print("Bästa lösningen använder ", pos.drag, " drag")
        exit()


    add(pos.r,   pos.k+1, pos.drag + 1) # Höger
    add(pos.r,   pos.k-1, pos.drag + 1) # Vänster
    add(pos.r+1, pos.k,   pos.drag + 1) # Nedåt
    add(pos.r-1, pos.k,   pos.drag + 1) # Uppåt


print("Ingen lösning!")






















