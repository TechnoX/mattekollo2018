# Kvadratens bredd och höjd.
N = int(input("Kvadratens sida? "))

#Minsta antalet drag som krävs är åtminstone inte
#fler än 2N, vilket är en enkel lösning där man
#bara placerat ut en stor fet kvadrat och övriga
#mindre kvadrater av storlek 1.
minsta = 2*N+1

# Vår kvadrat som vi ska fylla.
kvadrat = [[False for i in range(N)] for j in range(N)]


def findFirstEmpty():
    """ Metod som letar rätt på en ledig ruta och retunerar dess koordinat i form av en punkt. """
    for i in range(N): # y-koordinat.
        for j in range(N): # x-koordinat.
            # Om rutan är ledig så retunerar vi den.
            if not kvadrat[i][j]:
                return (j,i)
    # Kvadraten är full.
    return ()



def isValid(p, size):
    """
    Retunerar huruvida det är tillåtet att lägga en kvadrat av storlek size
    med sitt övre vänstra hörn i punkten/rutan p. Dvs metoden kollar att
    kvadraten man tänker lägga inte överlappar andra eller går utanför.
    """
    # För stora kvadrater tycker ingen om.
    if p[0] + size > N or p[1] + size > N:
        return False
    # Går igenom det område som kvadraten kommer att täcka.
    for i in range(p[1], p[1]+size): # y-koordinat.
        for j in range(p[0], p[0]+size): # x-koordinat.
            # Om rutan redan var upptagen så är draget otillåtet.
            if kvadrat[i][j]:
                return False
    # Kvadraten har klarat testerna.
    return True



def putQuad(p, size):
    """ Lägger en kvadrat av storlek size på punkten/rutan p."""
    # Markerar de rutor som kvadraten ska täcka som upptagna.
    for i in range(p[1], p[1]+size):
        for j in range(p[0], p[0]+size):
            kvadrat[i][j] = True


def removeQuad(p, size):
    """ Tar bort en kvadrat av storlek size som börjar i punkten p."""
    for i in range(p[1], p[1]+size):
        for j in range(p[0], p[0]+size):
            kvadrat[i][j] = False


def rek(used):
    """ Vår rekursiva metod som testar att lägga ut kvadrater. 
    used: Hur många kvadrater vi använt. """
    global minsta
    # Om vi redan har en bättre lösning, dumt att fortsätta.
    if used >= minsta:
        return
    # Hittar första tomma rutan.
    p = findFirstEmpty()

    # Om svaret var null så betyder det att kvadraten är full
    # och vi har funnit den hittills bästa lösningen.
    if not p:
        minsta = used
    else: # Annars så fortsätter vi att testa lägga ut kvadrater på punkten p.
        # Vi börjar att testa med större kvadrater. (Det är smartare.)
        for size in range(N-1, 0, -1):
            # Om det är tillåtet att lägga kvadraten så gör vi det.
            if isValid(p, size):
                # Lägger kvadraten med storleken size på punkten p.
                putQuad(p, size)
                
                # Nu har vi använt en kvadrat och testar att lägga på en annan punkt.
                rek(used+1)
                
                # Tar bort kvadraten, är ju inte säkert att den är optimal.
                removeQuad(p, size)



# Om sidan är jämn så är lösningen trivial.
if N%2 == 0:
    minsta = 4
else: # Annars får vi testa oss fram.
    # Från början har vi lagt ut noll mindre kvadrater.
    for i in range(1 + N//2,0,-1):
        #print(i)
        putQuad((0,0), i)
        rek(1)
        removeQuad((0,0), i)

#Skriver ut svaret.
print("Det behövs minst " + str(minsta) + " kvadrater")
