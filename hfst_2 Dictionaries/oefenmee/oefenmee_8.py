# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
# Vraag de gebruiker naar een stad. Print vervolgens de zin "Het is hier *temp* °C."
# Als de stad onbekend is, print dan in de plaats  "Het is hier ??? °C."
# Je moet de methode get() gebruiken tijdens deze oefening.

vraag_naarstad = input(f'welke stad je kan kiezen uit {",".join(steden_temp.keys())} ')
temperatuur = steden_temp.get(vraag_naarstad,"???" )

print(f'het is hier in {vraag_naarstad}  {temperatuur} graden ')