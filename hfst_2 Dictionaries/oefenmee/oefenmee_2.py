# . Kies zelf of je commentaar schrijft bij de code.
# Gebruik de dictionary fruitmand tijdens deze oefening.

# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,  #de appel is de key en de 5 is de waarde ervan dus als je wilt weten hoeveel appels er zijn kan je het zien aan de 5
    "banaan": 3,
    "kers": 50
}

# Niveau 2
# Gebruik onderstaande variabelen om een nieuw element toe te voegen aan de dictionary.
nieuw_fruit  = "mango"
nieuw_aantal = 1
fruitmand[nieuw_fruit] = nieuw_aantal

# Niveau 3
# Gebruik onderstaande variabelen om de waarde van een element in de dictionary te wijzigen.
fruit = "banaan"
nieuw_aantal = 8

print(fruitmand)

fruitmand[fruit] = nieuw_aantal

print(fruitmand)

# De dictionary erna printen geeft volgend resultaat.
	# {'appel': 5, 'banaan': 8, 'kers': 50, 'mango': 1}

# Niveau 4
# Gebruik onderstaande variabelen om de waarde van een element in de dictionary te verlagen.
fruit = "kers"
nieuw_aantal = 43

fruitmand[fruit] = fruitmand[fruit] -nieuw_aantal

print(fruitmand)
# De dictionary erna printen geeft volgend resultaat.
# 	{'appel': 5, 'banaan': 8, 'kers': 7, 'mango': 1}

# Niveau 5
# Gebruik onderstaande variabele om een element te verwijderen uit de dictionary.
terugleggen_fruit = "kers"

fruitmand.pop(terugleggen_fruit)

print(fruitmand)
# De dictionary erna printen geeft volgend resultaat.
# 	{'appel': 5, 'banaan': 8, 'mango': 1}

# De methode .pop() geeft ook iets terug. Zoek uit wat deze returnt. Je mag hiervoor gebruik maken van het internet of de tooltip van VS Code.
