antal = int(input("Antal travar ? "))
travar = []
for i in range(antal):
    travar.append(int(input("Böcker i trave "+ str(i+1) + "?")))

history = []

def seen_before(travar):
    for trave in history:
        if trave == travar:
            return True
    history.append(travar[:])
    return False

while not seen_before(travar):
    antal = 0
    i = 0
    while i  < len(travar):
        if travar[i] > 0:
            travar[i] -= 1
            antal += 1
        if travar[i] == 0:
            del travar[i]
        else:
            i += 1
    travar.append(antal)
    #print(travar)

print("Dag",len(history)+1,"uppkom ett upplägg som redan funnits förut")
