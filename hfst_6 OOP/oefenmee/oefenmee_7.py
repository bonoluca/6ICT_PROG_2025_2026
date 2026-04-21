# Werk verder met de klasse Hond van oefen mee 6.


" Stel de test voor niveau 3 zelf op. "

# Oefen mee 7
# Plak hierin de klasse hond die je in oefen mee 6 geschreven hebt. 

class Hond:
    klein = True

    def __init__(self, naam:str, leeftijd:int, massa:float, soort:str) -> None:
        self.naam = naam
        self.leeftijd = leeftijd
        self.massa = massa
        self.soort = soort
    
    def blaf(self ) ->None:
        print (f"{self.naam} zegt blaf")
    
    def weegschaal(self) -> None:
        print(f"{self.naam} weegt {self.massa} kg")
    
    def wijzig_naam(self, naam:str ):
        oude_naam = self.naam
        self.naam = naam 
        print(f"de hond zijn naam is van {oude_naam} naar {self.naam} gegaan")
    
    def eten(self ,hoeveelheid:float)-> None:
        self.massa = self.massa + hoeveelheid
        print(f"de nieuwe massa van {self.naam} is {self.massa}")


# Niveau 1
# Maak een nieuwe methode wijzig_naam aan. Hiermee kan je de eigenschap naam van de hond wijzigen. De methode print ook de oude & nieuwe naam van de hond. 

" Via onderstaande code kan je niveau 1 testen. "
hond = Hond("Lucky", 5, 13,"?") 
hond.wijzig_naam("Bolly")


" Via onderstaande code kan je niveau 2 testen. "
hond = Hond("Lucky", 5, 5, "?")
hond.eten(0.5)
hond.eten(0.5)
hond.eten(0.5)


# Maak een object van de klasse Hond aan. Deze heeft als starteigenschappen:
#         • naam: "Lucky"
#         • massa: 5

# Wijzig de naam naar "Bolly" met behulp van de methode wijzig_naam. Dit print:
# hond = Hond("Lucky", 5)
# hond.wijzig_naam("Bolly")

# Lucky heet nu Bolly.

# Niveau 2
# Maak een nieuwe methode eten aan. Deze heeft als parameters:
#         • self
#         • hoeveelheid (hoeveel eten de hond krijgt in kg).
# Deze methode oproepen, verhoogt de eigenschap massa met de waarde van hoeveelheid. De methode print ook telkens de naam van de hond & de nieuwe massa.

# Voer de methode 3 keer uit op het object uit niveau 1. 
# De waarde van hoeveelheid is 0.5. Dit geeft volgende boodschap.
# hond.eten(0.5)
# hond.eten(0.5)
# hond.eten(0.5)
# Bolly weegt nu 5.5kg.
# Bolly weegt nu 6.0kg.
# Bolly weegt nu 6.5kg.


# Niveau 3
# Maak een andere object van de klasse Hond aan (VB. hond_2).  De waarden van de eigenschappen kies je zelf (VB. 'Fleur' en 8). Voer voor dit object opnieuw 3x de methode eten uit. De waarde van hoeveelheid is 0.5.

# Niet al het eten zal bijdragen aan de massa van de hond. Slechts 30% van de hoeveelheid voer zal effectief omgezet worden naar massa. 

# Pas de methode eten aan. Verhoog massa van het object niet met hoeveelheid, 
# maar met 0.3*hoeveelheid. Voer hierna de code opnieuw uit. 
# Bolly weegt nu 5.15kg.
# Bolly weegt nu 5.30kg.
# Bolly weegt nu 5.45kg.
# Fleur weegt nu 8.15kg.
# Fleur weegt nu 8.3kg.
# Fleur weegt nu 8.45kg.

# Voor niveau 3 moest je nu slechts 1 regel wijzigen. Stel dat je de massa buiten de klasse had aangepast, hoeveel regels code moet je dan wijzigen?


