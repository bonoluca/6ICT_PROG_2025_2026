# Print de lengte van de acteurs in onderstaande lijst van dictionaries.
info_acteurs = [
    {"name": "Q. Tarentino", "leeftijd": 59, "lengte": 170},
    {"name": "J. Travolta", "leeftijd": 68, "lengte": 178},
    {"name": "S.L. Jackson", "leeftijd": 73},
    {"name": "U. Thurman", "leeftijd": 53, "lengte": 158}
]

for index, info_acteur in enumerate(info_acteurs):
    teller = 0
    print(info_acteur)
    naam = info_acteur['name']
    print(naam)

    if 'lengte' in info_acteurs:
        print(info_acteurs[naam])
    else:
        print('deze heeft geen lengte gegeven ')