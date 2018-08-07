wordlist = []
with open("ss100.txt", 'r') as f:
    wordlist = [line.strip() for line in f]
print(wordlist)
found = []
for a in "SFTN":
    for b in "MYOY":
        for c in "NASB":
            for d in "IREG":
                for e in "KLTD":
                    word = a+b+c+d+e
                    word = word.lower()
                    #print(word)
                    if word in wordlist:
                        found.append(word)
print(set(found))
