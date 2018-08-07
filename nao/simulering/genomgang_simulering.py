m = int(input("Talet m ? "))
n = int(input("Talet n ? "))

if m < n:
    print("Sätter växeln till läge m")
    vaxel = 'm'
else: 
    print("Sätter växeln till läge n")
    vaxel = 'n'

antal_andringar = 0
antal_minuter = 1440

for minut in range(1, antal_minuter):
    if minut % m == 0 and minut % n == 0:
        print("Båda tågen avgår på samma minut")
        if vaxel == 'n':
            # Vad ska vi göra?
            print("   Tåg n åker först")
            vaxel = 'm'
            antal_andringar += 1
            print("   Tåg m åker sen")
        else:
            print("   Tåg m åker först")
            vaxel = 'n'
            antal_andringar += 1
            print("   Tåg n åker sen")
            # Och här?


    elif minut % m == 0:
        print("Vid minut " + str(minut) + " avgår tåg m")
        if vaxel != 'm':         # Om växel är felställd
            vaxel = 'm'          # Sätter växeln i läge m
            antal_andringar += 1 # Ökar ändringarna som Loke måste göra
            print("   Loke ändrar växeln till läge m")

    elif minut % n == 0:
        print("Vid minut " + str(minut) + " avgår tåg n")
        if vaxel != 'n':         # Om växel är felställd
            vaxel = 'n'          # Sätter växel i läge n
            antal_andringar += 1 # Ökar ändringarna som Loke måste göra
            print("   Loke ändrar växeln till läge n")

print("Loke behövde ändra på växeln " + str(antal_andringar) + " gånger")



