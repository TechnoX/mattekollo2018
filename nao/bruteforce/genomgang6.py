ord = "BIL"

antal = 0
for bokstav in ord: 
    for bokstav2 in ord:
        if bokstav == bokstav2: continue
        for bokstav3 in ord: 
            if bokstav==bokstav3 or bokstav2==bokstav3: continue
            
            print(bokstav, bokstav2, bokstav3)
            antal += 1

print("Det finns totalt "+ str(antal) + " sätt att skapa ord av bokstäverna BIL")
print("\n\n\n\n")


for red in range(100):
    for green in range(100):
        for yellow in range(100):
            if red + red + red == 90:
                if red + 2*green + 2*green == 230:
                    if yellow + 2*green + red == 210:
                        print("Yellow: ", yellow)
                        print("Red: ", red)
                        print("Green: ", green)
                        print("Answer: ", green - red + yellow)
                        print("-------------------------------")


