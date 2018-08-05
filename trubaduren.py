antal_personer = int(input("Antal personer? "))
antal_dagar = int(input("Antal dagar? "))
dagar = []
for d in range(antal_dagar):
    rad = input("Dag " + str(d+1) + "? ").split(" ")
    dagar.append([int(d) for d in rad])


# Vilka bybor som kan vilken sång
songs = []

# Returnerar en lista på alla sånger som den specifika personen kan
def known_songs(person):
    known = []
    for song_index, persons in enumerate(songs):
        #print("Kollar om " + str(person) + " kan sång " + str(song_index) + " som " + str(persons) + " kan")
        if person in persons:
            #print("Ja, hen kunde, så lägger till " + str(song_index) + " till hens repertoar")
            known.append(song_index)
    return known

# Lär personen alla dagens låtar som hen inte redan kan. 
def learn_songs(person, todays_songs):
    for song_index in todays_songs:
        # Om personen inte redan kan låten, så har han lärt sig den
        if not person in songs[song_index]:
            print("Person " + str(person) + " lärde sig låt " + str(song_index))
            songs[song_index].append(person)

for dag_index, personer_narvarande in enumerate(dagar):
    # Om trubadur medverkar
    if 1 in personer_narvarande:
        print(" # Trubaduren medverkar dag "+str(dag_index+1)+" och lär dem låt " + str(len(songs)))
        todays_songs = [len(songs)]
        songs.append(personer_narvarande)
    else: # Annar sjunger de för varandra
        print(" # De sjunger alla låtar på dag " + str(dag_index+1))
        todays_songs = []
        for person in personer_narvarande:
            todays_songs.extend(known_songs(person))
        #todays_songs = set(todays_songs) # Tar bort duplicerade låtar
    
    print("Dagens låtlista: " + str(todays_songs))
    # Uppdaterar personerna med vad de lärt sig för nya låtar idag
    for person in personer_narvarande:
        learn_songs(person, todays_songs)

print("################\n")
# Skriver ut de som kan alla låtar
for person in range(1,antal_personer+1):
    if len(known_songs(person)) == len(songs):
        print("Person " + str(person) + " kan alla låtar")
