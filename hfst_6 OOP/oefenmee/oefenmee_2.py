# Oefen mee 2
# Plak hierin de code die je in oefen mee 1 geschreven hebt. 

class KleineHond:
    klein = True

    def __init__(self, naam:str, leeftijd:int, massa:float, soort:str) -> None:
        self.naam = naam
        self.leeftijd = leeftijd
        self.massa = massa
        self.soort = soort
    
    def hondblaft(self ) ->None:
        print (f"{self.naam} zegt blaf")
    
    def weegschaal(self) -> None:
        print(f"{self.naam} weegt {self.massa} kg")

hond1 = KleineHond("kico", 13, 13, "Jack Russel")

hond1.hondblaft()

hond1.weegschaal()

print(f'de naam van de hond is {hond1.naam} de massa is {hond1.massa}')


# Niveau 1
# Voeg aan de klasse Hond nu ook een methode blaf toe. 
# Oproepen van deze methode print: *naam van hond* zegt blaf.

# Voer deze methode uit met 2 objecten van de klasse Hond.

# Niveau 2
# Maak een nieuwe methode weegschaal aan. Schrijf nu "zichzelf" in plaats van "self" als parameter. Hoe kan je nu volgende zin printen: *naam van hond* weegt *massa*kg .

# Niveau 3
# Waarom moet je niets tussen de haken van methoden schrijven tijdens het oproepen?
# Met andere woorden, hoe weet Python welke waarde self is?
#doordat je die eerder gebruikt 


