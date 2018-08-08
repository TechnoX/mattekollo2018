
antal_stenblock = 35 # = 1*1 + 3*3 + 5*5, höjd = 3
antal_stenblock = 165 # = 1*1 + 3*3 + 5*5 + 7*7 + 9*9 - 1, höjd = 4
antal_stenblock = 456 # = 1*1 + 3*3 + 5*5 + 7*7 + 9*9 + 11*11 + 13*13 + 1, höjd = 7
antal_stenblock = 12347930

antal_stenblock = int(input("Antal stenblock: "))

antal_stenblock_använda = 0
höjd = 0
while True:
    antal_stenblock_till_nästa_höjd = (höjd*2 + 1)**2
    if antal_stenblock_till_nästa_höjd <= antal_stenblock-antal_stenblock_använda:
        antal_stenblock_använda += antal_stenblock_till_nästa_höjd
        höjd += 1
    else:
        break
print(höjd)

"""
kuber = 0
for i in range(210):
    kuber += (i*2 + 1)**2
print(kuber)
"""
