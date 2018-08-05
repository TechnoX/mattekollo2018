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


hojd = len(karta)
bredd = len(karta[0])
print(hojd)
print(bredd)

# Håller reda på bästa lösningen.
min_drag = 1000000

# Håller reda på om positionen är besökt
besokt = [[False for b in range(bredd)] for h in range(hojd)]

class position():
    def __init__(self, r, k, drag):
        self.r = r
        self.k = k
        self.drag = drag # Drag det tagit för att komma till denna position


lista = [position(start[0], start[1], 0)]

def add(r, k, drag):
    """ 
    Funktion som lägger till situationen sist i kön.
    r, k = koordinaterna för denna situation
    drag = antal drag som behövdes för att komma hit
    """
    if karta[r][k] == '#':
        # Omöjlig position i kartan
        return
    if besokt[r][k]:
        # Redan besökt plats
        return
    pos = position(r, k, drag)
    lista.insert(0, pos)
    besokt[r][k] = True

while lista:
    # Nuvarande position
    pos = lista.pop()
    if pos.r == slut[0] and pos.k == slut[1]:
        print("Bästa lösning använder ", pos.drag, " drag")
        exit()
    add(pos.r,   pos.k+1, pos.drag + 1) # Höger
    add(pos.r,   pos.k-1, pos.drag + 1) # Vänster
    add(pos.r+1, pos.k,   pos.drag + 1) # Nedåt
    add(pos.r-1, pos.k,   pos.drag + 1) # Uppåt
    
print("Ingen lösning!")


