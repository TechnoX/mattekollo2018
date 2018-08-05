from time import sleep


## Läs in kartan

with open("karta.txt", 'r') as f:
    line = f.readline().strip()
    start = line.split(',')
    start = [int(e) for e in start]
    line = f.readline().strip()
    slut = line.split(',')
    slut = [int(e) for e in slut]
    resten = f.read()
    karta = resten.split('\n')
    karta = karta[:-1]
    
print("done")
print(karta)
print(start)
print(slut)
hojd = len(karta)
bredd = len(karta[0])

# Håller reda på bästa lösningen. Det stora värdet betyder ingen lösning hittad
min_drag = 1000000

# Håller reda på om positionen är besökt. 
besokt = [[False for b in range(bredd)] for h in range(hojd)]


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

def go(r, k, num):
    global min_drag
    """
    Rekursiv funktion som "går runt" i labyrinten
    x, y  =  koordinaterna just nu
    num = antal drag hittills
    """
    if karta[r][k] == '#':
        # Omöjlig position i kartan
        return
    if besokt[r][k]:
        # Redan besökt plats
        return
    if num >= min_drag - 1:
        # Onödigt att leta om det inte går att hitta någon bättre lösning.
        return
    if r == slut[0] and k == slut[1]:
        # Hittad lösning
        min_drag = num

    besokt[r][k] = True
    #visualisera()
    go(r,   k+1, num + 1) # Höger
    go(r,   k-1, num + 1) # Vänster
    go(r+1, k,   num + 1) # Nedåt
    go(r-1, k,   num + 1) # Uppåt
    
    besokt[r][k] = False


go(start[0], start[1], 0)

if min_drag == 1000000:
    print("Ingen lösning!")
else:
    print("Bästa lösning använder ", min_drag, " drag")



