# Oefen mee 1
# Niveau 1
# Maak een eigen klasse Hond. Geef deze klasse Hond volgende attributen:
#         • naam 
#         • massa
# Je mag de waarden van deze attributen zelf kiezen. VB. "Fido" & 6.

# Niveau 2
# Maak twee objecten van de klasse Hond. Gebruik volgende variabelnamen:
#         • hond !! Let op: kleine letters voor object !!
#         • huisdier

# Niveau 3
# Print voor ieder object volgende zaken:
#         • naam 
#         • massa
#         • Datatype van het object (via functie type)

class KleineHond:
    klein = True

    def __init__(self, naam:str, leeftijd:int, massa:float, soort:str) -> None:
        self.naam = naam
        self.leeftijd = leeftijd
        self.massa = massa
        self.soort = soort
    


hond1 = KleineHond("kico", 13, 13, "Jack Russel")
huisdier = KleineHond()

print(f'de naam van de hond is {hond1.naam} de massa is {hond1.massa} en de ')

