# Start de oefen mee met onderstaande dictionary.
persoonsinfo = { # info over een persoon
    "naam": "Jan",
    "leeftijd": 32,
    "massa": 79
}

# Gebruik de info in de dictionary om volgende zin te printen.
# De code moet blijven werken, ook als de waarden van het element in de dictionary wijzigt.
# Tip! Gebruik een f-string.

# Jan is 32 jaar oud & weegt 79 kg.

print(f'{persoonsinfo["naam"]} is {persoonsinfo["leeftijd"]} en weegt {persoonsinfo["massa"]}')

# Niveau 2
# Voer onderstaande code uit.
print( len( persoonsinfo ) )

# Wat is de betekenis van het getal dat len( persoonsinfo ) teruggeeft?

"deze code print de lengte van hoeveel waardes we hebben "

# Niveau 3
# # Voer onderstaande code uit. 
# oogkleur = persoonsinfo["oogkleur"]
# print(f"Deze persoon heeft {oogkleur} ogen.")


# # Er verschijnt een foutmelding in de terminal. Welke? Leg ook uit wat deze foutmelding betekent.
# """de foutmelding error : er zit dan een fout in je code  
# er moet staan"""

# persoonsinfo["oogkleur"] = "groene"
# print(f'deze persoon heeft {persoonsinfo["oogkleur"]} ogen ')

# Niveau 4
# Voer onderstaande code uit (vergeet niet de code van Niveau 3 in commentaar te zetten).
naam = "Jan"
print(persoonsinfo[naam])

# Deze code leidt tot dezelfde foutmelding als in Niveau 3. 
# Hoe kan dit? "Jan" komt toch voor in de dictionary.

"dat komt omdat naam dus jan is de key en je hebt dan nog altijd geen waarde toegevoegd "

