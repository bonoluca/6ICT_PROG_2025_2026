# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

# Niveau 1
# Gebruik input() om de gebruiker naar een sleutel in jouw dictionary te vragen.
# Print vervolgens de waarde die overeenkomt met deze sleutel.

welke_fruit = input(f'welke fruit wil je. je kan kiezen uit {",".join(fruitmand.keys())} ')

if welke_fruit in fruitmand:
    print(f'er zijn {fruitmand[welke_fruit]} {welke_fruit} in jou mand ')
else:
    print("die fruit is er niet ")


#         Voorbeeld in terminal (maakt gebruik van de dictionary fruitmand):
#         Welk soort fruit zoek je: banaan
#         Aantal banaan in mand: 3
#         input
# print

# Niveau 2
# Een gebruiker kan opgeven wat deze wilt. Volgende situatie kan momenteel dus ook optreden.
#         Welk soort fruit zoek je: friet
#         KeyError: 'friet'
#         input
# foutmelding
        
# We willen dit niet. Er moet dus eerst gecontroleerd worden of de input van de gebruiker effectief in de dictionary zit. Voeg volgende functionaliteit toe aan de code.
#         • Sleutel bestaat: voer code uit Niveau 1 uit.
#         • Sleutel bestaat niet: print 'Kon *input* niet vinden in de fruitmand.'

#         Tip! Gebruik if ... In ... om te controleren of de input van de gebruiker in de dictionary bestaat.

# Een niet-bestaande sleutel als input heeft nu volgend resultaat.
#         Welk soort fruit zoek je: friet
#         Kon friet niet vinden in de fruitmand.
#         input
# print
        



