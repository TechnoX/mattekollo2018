
rad = input("Papperslappar ? ").split(" ")
answers = [int(e) for e in rad]#[80, 82, 83, 84, 85, 86, 87, 88, 90, 91]

for a in range(50):
    for b in range(a,50):
        for c in range(b,50):
            for d in range(c,50):
                for e in range(d,50):
                    if sorted([a+b, a+c, a+d, a+e, b+c, b+d, b+e, c+d, c+e, d+e]) == answers:
                        print(a,b,c,d,e)
