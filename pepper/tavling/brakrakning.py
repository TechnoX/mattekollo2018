#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nämnarna till våra bråk som vi får bilda summor av.
namnarna = [1,2,3,4,5,6,7,8,9,10]
# Täljarna till våra bråk, när vi har förlängt alla till gemensam nämnare.
# Alla initieras till 0. Om en täljare senare fortfarande är 0, så betyder det
# att det bråket inte är kompatibelt med bråket som användaren har matat in.
taljarna = [0] * len(namnarna)
# Täljaren som användaren ska ange.
taljare = input("Täljare ? ")
# Nämnaren som användaren ska ange.
namnare = input("Nämnare ? ")

# Sparar talföljden av bråk som kunde bilda det önskade bråket.
# Om längden på strängen frotfarande är 0 vid programmets slut
# så betyder det att uppgiften var omöjlig.
successful = ""



def rek(frac, sequence, i):
    """
    Vår rekursiva funktion som ska lösa problemet.
    frac: Täljaren till det bråk vi för tillfället har. Nämnaren behöver vi inte
    hålla reda på eftrsom den är densamma för alla.
    sequence: Talföljden av bråk som ledde fram till vårt nuvarande.
    int i: Indexet för det bråk vi är på och ska testa att lägga till på talföljden.
    """
    global successful

    # Om vår täljare är = den önskade täljaren så har vi lyckats.
    if frac == taljare:
	# Sparar talföljden som ledde fram till svaret.
	successful = sequence
	# Returnerar, det är ju dumt att lägga till bråk på ett bråk som redan är rätt.
	return

    # Om vårt bråk redan är större än det önskade, så behöver vi ju inte fortsätta
    # att lägga till bråk på talföljden.
    elif frac > taljare:
        return

    # Eller om vi redan har avverkat alla bråk, då ska man avbryta.
    elif i >= len(namnarna):
	return



    # Om detta bråk är kompatibelt med vårt bråk.
    if taljarna[i] != 0: 
	# Lägger till bråket på talföljden.
	rek(frac+taljarna[i], sequence+"1/"+str(namnarna[i])+" ", i+1)

    # Bara för att bråket är kompatibelt, så behöver ju inte det betyda att det ska ingå i den korrekta talfölden.
    # Att testa att inte ta med bråket är minst lika viktigt.
    rek(frac, sequence, i+1)






# Loopar igenom alla bråk och kollar om de funkar tillsammans med det inmatade bråket.
for i in range(len(namnarna)):
    # Om den inmatade nämnaren är jämnt delbar med nuvarande bråks nämnare, så är bråket kompatibelt.
    if namnare % namnarna[i] == 0:
	# Om vi förlänger bråket till det inmatade bråkets nämnare, så kommer alla bråken såklart få samma nämnare.
        # Det enda som skiljer sig är täljaren. Alltså behöver vi bara hålla koll på täljaren som vi ska addera. 
	taljarna[i] = namnare/namnarna[i]
    # Om inte så förblir täljaren till bråket 0, vilket indikerar att bråket inte är kompatibelt.

print(taljarna)
# Nu ska vi hitta talföljden, det enda vi behöver göra är att addera ihop våra täljare som vi har tagit fram
# i loopen ovan tills vi får samma täljare som användaren har matat in. Lätt som en plätt.
# Vi börjar så klart med 0 (vi har inte adderat några täljare ännu), en tom sträng (inga tal ingår i talföljden än så länge)
# och vi ska börja att testa med det första bråket (täljaren) som har index 0.
rek(0, "", 0)




# Om strängen som har svaret inte har längden 0, så finns det ett svar.
if len(successful):
    print("Termer: " + successful)
# Om den är 0 så var visst uppgiften omöjlig.
else:
    print("Omöjligt")

