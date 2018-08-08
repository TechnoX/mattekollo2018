N = 10 #Antalet dagar, 1<=N<=100
H = 27 #snötröskel - när det är så här många cm snö MÅSTE det skottas, 1<=H<=1000

#snöförändring - ett heltal mellan -100 och 100 (inklusive). Negativt värde = smälter, positivt värde = snöar
snöförändring = [5, -7, 8, 19, -20, 22, 8, 26, -15, 14]

snö_på_marken = 0 #Uppdaterar snön på marken varje dag
antal_skottningar = 0 #Uppdaterar antal skottningar som måste göras
for i in range(N):
    snö_på_marken += snöförändring[i] #lägger till snön som kom över natten till gårdagens snö
    if snö_på_marken >= H: #kollar om snön är över/lika med max-gränsen
        snö_på_marken = 0 #nollställer isf snön (all snö är bortskottad)
        antal_skottningar += 1 #lägger till att vi har skottat en gång
    if snö_på_marken < 0: #kollar om det finns möjlighet att smälta mer snö än det finns
        snö_på_marken = 0 #nollställer isf snön (så det inte kan vara negativ snö)
        
print("Scott behöver skotta minst ", antal_skottningar, " gånger.")
