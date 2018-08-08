# coding=utf-8
m = int(input("Talet m ? ")) 
n = int(input("Talet n ? "))

if m > n:
    print("Sätter växeln till n")
    vaxel = 'n'
else:
    print("Sätter växeln till m")
    vaxel = 'm'

antal_andringar = 0
antal_minuter = 1440

# Start simulering
for minut in range(1, antal_minuter):
    
    if minut % m == 0 and minut % n == 0:
        print("Båda tågen kommer samtidigt, efter " + str(minut) + " minuter")
        if vaxel == 'm':
            print(" - Ändrar växeln till n")
            vaxel = 'n'
        else:
            print(" - Ändrar växeln till m")
            vaxel = 'm'
        antal_andringar += 1
    elif minut % m == 0:
        print("Tåg m kommer efter " + str(minut) + " minuter")
        if vaxel != 'm':
            print(" - Ändrar växeln till m")
            vaxel = 'm'
            antal_andringar += 1
    elif minut % n == 0:
        print("Tåg n kommer efter " + str(minut) + " minuter")
        if vaxel != 'n':
            print(" - Ändrar växeln till n")
            vaxel = 'n'
            antal_andringar += 1

print("Antal vaxlingar:" + str(antal_andringar))
