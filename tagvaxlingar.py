print("Tågen går med m respektive n minuters mellanrum.")
m = int(input("Talet m = ")) #Ena tåget avgår var m-te minut
n = int(input("Talet n = ")) #Andra tåget avgår var n-te minut

N = 1440 # antal minuter på ett dygn


antal_växeländringar = 0 #Räknar antalet gånger Loke måste växla
for minuter in range(N): #Räknar fram till minut 1440 (0-1439, minut 1440 ej påbörjad)
    if minuter == 0:
        if m>n: #Spåret börjar på den sidan vars tåg åker iväg först. Behöver därför inte växla spår.
            spak = "n"
        else:
            spak = "m"
    elif minuter%m == 0 and minuter%n == 0: #kollar om båda tågen avgår från stationen samtidigt
        if spak == "m": #Tåget vars spår redan är växlad rätt kör först, därefter växlar Loke och det andra tåget kan köra iväg
            spak = "n"
            antal_växeländringar += 1
        else:
            spak = "m"
            antal_växeländringar += 1
    elif minuter%m == 0: #Om enbart det ena tåget är vid stationen
        if spak != "m": #kollar om det är nödvändigt att växla
            spak = "m"
            antal_växeländringar += 1
    elif minuter%n == 0: #Om enbart det andra tåget är vid stationen
        if spak != "n": #kollar om det är nödvändigt att växla
            spak = "n"
            antal_växeländringar += 1

print("Antal växlingar: ", antal_växeländringar)
