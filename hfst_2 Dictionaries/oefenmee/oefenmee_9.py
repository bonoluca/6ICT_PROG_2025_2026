# Start de oefen mee met onderstaande dictionary.


recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}

print(recept)

# print("Recept voor worst met wortelen en erwten.")


for sleutel, waarde in recept.items():
    print(sleutel,waarde)

# Print de zin "Recept voor worst met wortelen en erwten."

# Overloop nu de verschillende ingrediënten van dit recept. Ieder ingrediënt moet apart geprint worden. 
# De te printen regel is "- *ingrediënt*: *hoeveelheid* gr.
# De methode items() dient tijdens deze opdracht gebruikt te worden.

# 	In de opdrachtprompt ziet dit er als volgt uit.
# 	Recept voor worst met wortelen en erwten.	print
# print
# print
# print
# print
# 	 - Aardappelen: 800 gr.
# 	 - Wortelen: 500 gr.
# 	 - erwten: 300 gr.
# 	 - Worsten: 400 gr.


# niveau2

vraag_naar_hvl_man = int(input('voor hoeveel man wil je dit recept klaar maken '))
schaal = vraag_naar_hvl_man / 4
print("Recept voor gehakt met wortelen en erwten.")
for sleutel, waarde in recept.items():
    waarde = waarde * schaal     
    print(sleutel,waarde)

# Dit recept is bedoeld voor groepen van 4. Vraag aan de gebruiker voor hoeveel hij
# dit gerecht wilt klaarmaken. Schaal de hoeveelheid eten naar dit aantal. Rond hoeveelheden altijd naar beneden af.

# 	In de opdrachtprompt ziet dit er als volgt uit.
# Voor hoeveel man kook je: 7
# Recept voor gehakt met wortelen en erwten.
#  - Aardappelen: 1400 gr.
#  - Wortelen: 875 gr.
#  - erwten: 525 gr.
#  - Worsten: 700 gr.
