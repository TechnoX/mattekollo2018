langder = {}
hoger = {}
vanster = {}
for b in "ABCDEFGH":
    v = int(input("Barn "+b+", vänster? "))
    h = int(input("Barn "+b+", höger? "))
    vanster[b] = v
    hoger[b] = h
    langder[b] = 8 - v - h
print("Vänster: ", str(vanster))
print("Höger: ", str(hoger))
print("Längder: ", str(langder))

for k in "ABCDEFGH":
    for l in "ABCDEFGH":
        if l==k: continue
        for m in "ABCDEFGH":
            if m==k or m==l: continue
            for n in "ABCDEFGH":
                if n==k or n==l or n==m: continue
                for o in "ABCDEFGH":
                    if o==k or o==l or o==m or o==n: continue
                    for p in "ABCDEFGH":
                        if p==k or p==l or p==m or p==n or p==o: continue
                        for q in "ABCDEFGH":
                            if q==k or q==l or q==m or q==n or q==o or q==p: continue
                            for r in "ABCDEFGH":
                                if r==k or r==l or r==m or r==n or r==o or r==p or r==q: continue
                                print(k,l,m,n,o,p,q,r)
                                seq = (k+l+m+n+o+p+q+r)
                                for index, letter in enumerate(seq):
                                    h = sum([langder[b]>langder[letter] for b in seq[index:]])
                                    v = sum([langder[b]>langder[letter] for b in seq[:index]])
                                    print("Höger: ", h, ", Vänster: ", v)
                                    if h == hoger[b] and v == vanster[b]:
                                        print("Stämmer!")
                                        exit()
                                
