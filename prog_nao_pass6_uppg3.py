N = int(input("N = "))
antal_trianglar = 0
for a in range(1,N+1): # Testar alla tal 1 till N för a
    for b in range(1,N+1): # Testar alla tal 1 till N för b
        for c in range(1,N+1): # Testar alla tal 1 till N för c
            if (c**2) == (a**2 + b**2 - a*b): # testar att formeln stämmer
                antal_trianglar += 1 #lägger då till en triangel
"""
Antalet trianglar som är beräknade 2 gånger
(spegelvända, a->b, b->a) = antal_trianglar-N
Eftersom det finns N stycken trianglar som är liksidiga,
resten ger dubbletter. Måste därefter addera N igen:
"""
print("antal trianglar: ", int((antal_trianglar-N)/2 + N))
