karta = []
# Läser in kartan
while True:
    rad = input()
    if not rad:
        break
    karta.append(list(rad))


# Börjar simuleringen
x = 0
y = 0
while True:
    if karta[y][x] == 'B':
        print("Roboten kommer gå till Batteriet")
        break
    if karta[y][x] == 'E':
        print("Roboten kommer få en Elstöt")
        break
    if karta[y][x] == 'X':
        print("Roboten kommer gå runt, runt, runt för evigt")
        break

    # Eftersom vi skriver över värdet i kartan så sparar vi undan det först
    # Så vi kan minnas var vi ska förflytta oss i kartan
    riktning = karta[y][x]
     # Sätt rutan till besökt
    karta[y][x] = 'X'
    
    if riktning == 'v':
        y+=1
    elif riktning == '^':
        y-=1
    elif riktning == '<':
        x-=1
    elif riktning == '>':
        x+=1

