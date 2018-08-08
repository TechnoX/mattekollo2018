"""
#----- Exempel -----
# person = [antal högre personer till vänster, antal högre personer till höger]
A = [1,2]
B = [3,1]
C = [1,0]
D = [0,0]
E = [2,0]
personer = {'A':A, 'B':B, 'C':C, 'D':D, 'E':E}
#Ger uppställningen: D A C B E
"""
A = [2,0]
B = [0,1]
C = [0,6]
D = [2,3]
E = [0,0]
F = [3,1]
G = [2,1]
H = [6,1]
personer = {'A':A, 'B':B, 'C':C, 'D':D, 'E':E, 'F':F, 'G':G, 'H':H}

langdordning = [] #längdorning, längst till kortast
uppstallning = [] #ordningen dom står i
for i in range(len(personer)):
    langdordning.append("") #skapar tomma listor med samma längd som antalet personer
    uppstallning.append("")

for person in personer: #jämför längden på personerna och lägger till dom i storleksordning
    antal_langre_personer = personer[person][0] + personer[person][1]
    langdordning[antal_langre_personer] = person

for person in langdordning: #kollar personerna i längdordning och placerar dom på rätt plats
    antal_personer_till_vanster = personer[person][0] #antal personer till vänster
    #flyttar personerna som ska ligga till höger om personen ett steg till höger, och gör plats för personen vi ser på:
    uppstallning[antal_personer_till_vanster+1:] = uppstallning[antal_personer_till_vanster:-1]
    uppstallning[antal_personer_till_vanster] = person #personen tar samma index som antalet personer till vänster
    
print("uppställning: ", uppstallning)
