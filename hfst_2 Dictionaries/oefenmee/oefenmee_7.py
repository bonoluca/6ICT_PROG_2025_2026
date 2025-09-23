# Start de oefen mee met onderstaande dictionary.


gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}

# Stel een while-loop op. Vraag via input() naar de naam van de gebruiker.
# 	• Staat de naam in de gastenlijst?
# Verwijder het overeenkomend element dan uit de dictionary (via pop).
# Print hierna de zin: "Welkom *job* *naam*. Kom binnen."
# 	• Staat de naam niet op de gastenlijst?
# Print dan "De naam *naam* staat niet op de lijst.
# De while-loop stopt als de gebruiker STOP ingeeft bij de input.

start = True

while start:
    vraag_naam = input('wat is jou naam ')
    if vraag_naam in gasten:
        print(f'Welkom {gasten[vraag_naam]} {vraag_naam}. Kom binnen.')
        gasten.pop(vraag_naam)
   
    elif vraag_naam == 'STOP':
        start = False

    elif vraag_naam not in gasten:
        print(f'de naam {vraag_naam} staat niet op de lijst')
   

