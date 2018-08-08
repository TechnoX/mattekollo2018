N = int(input("Talet N ? "))
antal = 0
for a in range(1,N+1):
    for b in range(a,N+1):
        for c in range(1,N+1):
            if c*c == a*a + b*b - a*b:
                print(a,b,c)
                antal += 1
print("Antal trianglar: ",antal)
