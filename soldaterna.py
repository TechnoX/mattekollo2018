persons = input("Soldater?")
count = 0 # antalet vändningar
while "HV" in persons: # så länge minst två soldater står bredvid varandra
    persons = persons.replace("HV", "VH") #vänd soldaterna
    count += 1
print(count)
