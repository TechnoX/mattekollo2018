vinkel = int(input("Vinkel = "))

vinkel_timme = 0 #startar med 0 grader vid 00:00
for timme in range(12): #För alla timmar på förmiddagen
    vinkel_minut = 0 #startar med 0 grader vid varje hel timme
    for minut in range(60): #För alla minuter
        if vinkel_minut>vinkel_timme: #kollar om vi får en positiv vinkelskillnad från timmvisare till minutvisare
            if (vinkel_minut-vinkel_timme) == vinkel: #om vinkelskillnaden är lika med den önskade vinkeln
                if minut < 10: #för fin utskrift kollar vi storleken på minuter
                    print(str(timme)+":0" +str(minut)) #lägger till en nolla före minutrarna ifall vi har ett ental
                else:
                    print(str(timme)+":"+str(minut)) #annars skrivs det ut som det är
        else:
            if 3600-(vinkel_timme-vinkel_minut) == vinkel: #om vinkelskillnaden är negativ lägger vi till 360 grader
                if minut < 10:
                    print(str(timme)+":0" +str(minut))
                else:
                    print(str(timme)+":"+str(minut))
        vinkel_timme += 5 #360 grader/60 minuter/12 timmar, 1 min på timmvisaren = 0.5 grader
        vinkel_minut += 60 #360 grader/60 minuter, 1 min på minutvisaren = 6 grader
