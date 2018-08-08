antal_kandidater = 9
Leonid_röster = 6
andras_röster = [4,3,8,4,4,16,18,2]

andras_röster.sort()
andras_röster.reverse()

antal_mutor = 0
while Leonid_röster <= andras_röster[0]:
    Leonid_röster += 1
    andras_röster[0] -= 1
    andras_röster.sort()
    andras_röster.reverse()
    antal_mutor += 1


print("Leonids röster: ", Leonid_röster)
print("De andras röster efter mutning: ", andras_röster)
print("Antal mutor Leonid måste köpa: ", antal_mutor)
