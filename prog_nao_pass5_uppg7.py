from numpy import zeros
N = int(input("Antalet personer i byn: ")) # 1<=N<=100
M = int(input("Antalet kvällar det sjungs visor i byn: ")) # 1<=N<=50

dagar = []
for i in range(M):
    en_dag = [int(x) for x in input("Närvarande bybor, dag%s: "%(i+1)).split()]
    dagar.append(en_dag)

personer = []
personer_som_kan_sanger = {}
for i in range(N):
    personer.append(i+1)
    personer_som_kan_sanger[i+1] = ""
    

nya_sanger = {}
i = 1
for dag in dagar:
    for person in dag:
        if person == 1:
            nya_sanger[i] = dag
            for bybo in dag:
                if personer_som_kan_sanger[bybo] == "":
                    personer_som_kan_sanger[bybo] = str(i)
                else:
                    personer_som_kan_sanger[bybo] += str(i)
            i += 1

print(personer_som_kan_sanger)
"""
song_number = 0
for dag in dagar:  # antal nätter totalt
    if dag == nya_sanger[song_number+1]:
"""
    
"""
sang = 1
for i in range(M):
    if dagar[i] != nya_sanger[sang]:
        for sangare in nya_sanger[sang-1]:
            for bybo in dagar[i]:
                if bybo == sangare:
                    nya_sanger[sang-1] += dagar[i]
                    print(nya_sanger)
                    nya_sanger[sang-1] = list(set(nya_sanger[sang-1]))
                   
    else:
        sang += 1
        if sang > len(nya_sanger):
            break
        
personer_som_kan_alla_sanger = []

for i in range(1,N+1):
    antal_sanger_personen_kan = 0
    for sang in nya_sanger:
        for bybo in nya_sanger[sang]:
            if i == bybo:
                antal_sanger_personen_kan += 1
    if antal_sanger_personen_kan == len(nya_sanger):
        personer_som_kan_alla_sanger.append(i)
    



print(personer_som_kan_alla_sanger)
"""

