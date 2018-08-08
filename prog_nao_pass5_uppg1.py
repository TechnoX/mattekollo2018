print("Skriv de 3 första talen i talföljden")
tal1 = int(input("Första talet: ")) #får in de 3 första talen i talföljden
tal2 = int(input("Andra talet: "))
tal3= int(input("Tredje talet: "))

skillnad1 = tal2-tal1 #tar ut skillnaden mellan de 2 första talen
skillnad2 = tal3-tal2 # tar ut skillnaden mellan tal 2 och tal 3

skillnad = skillnad2 - skillnad1 #jämför de 2 skillnaderna för att se hur mycket skillnaden ökar

temp_skillnad = skillnad2 #temporär skillnad. Skillnaden mellan varje enskilt tal
#Här väljer man antingen att skriva en lista (enklare) eller en string med alla svar (Det är detta uppgiften frågar om)
tal = [tal1, tal2, tal3] #För att skapa lista (med komma och hakparantes)
string = "%s %s %s"%(tal1, tal2, tal3) #för att skapa en string med mellanrum
for i in range(3,10):
    # Ser på talet innan i talföljden och adderar skillnaden mellan de 2 talen innan samt adderar skillnaden mellan alla skillnader
    tal.append(tal[i-1]+skillnad+temp_skillnad)
    string += " %s" %(tal[i-1]+skillnad+temp_skillnad)
    temp_skillnad += skillnad #ökar skillnaden mellan 2 tal allt eftersom
#Skriver ut en lista eller en string med tal, beroende på vad man valt att göra.
print(tal)
print(string)
