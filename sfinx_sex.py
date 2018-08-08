
#hannar = ["ML", "FG"]
#honor = ["VM", "FM", "VF"]
#alla_varelser = ["ML", "FG", "VM", "FM", "VF"]

alla_varelser = [None]

hannar = []
antal_hannar = int(input("Antal hannar: "))
for i in range(antal_hannar):
    hane = input("Skriv in hane nr%s : " %(i+1))
    hannar.append(hane)
    for varelse in alla_varelser:
        if varelse == hane:
                break
        if varelse == alla_varelser[-1]:
            alla_varelser.append(hane)
honor = []
antal_honor = int(input("Antal honor: "))
for i in range(antal_honor):
    hona = input("Skriv in hona nr%s : " %(i+1))
    honor.append(hona)
    for varelse in alla_varelser:
        if varelse == hona:
                break
        if varelse == alla_varelser[-1]:
            alla_varelser.append(hona)
   
for hane in hannar:
    for hona in honor:
        for varelse in alla_varelser:
            if varelse == hane[0]+hona[1]:
                break
            if varelse == alla_varelser[-1]:
                alla_varelser.append(hane[0]+hona[1])
        for varelse in alla_varelser:
            if varelse == hona[0]+hane[1]:
                break
            if varelse == alla_varelser[-1]:
                alla_varelser.append(hona[0]+hane[1])
#alla_varelser.pop(0) # Kan använda .pop(0) eller del 
del alla_varelser[0]
print(alla_varelser)
print(len(alla_varelser))

