# Maak de klasse Persoon & Hond aan zoals omschreven in oefen mee 10.
# Je start reeds met de __init__ van beide klassen.

# Niveau 1
# Voeg aan de klasse Persoon twee methoden toe (zaken tussen ** zijn eigenschappen):
# Methode	Parameter(s)	Uitleg
# koop_hond	self, hond	Voeg *naam* van hond toe aan *honden* persoon.
# Verander *eigenaar* in hond naar *naam* persoon.
# is_eigenaar	self, hond	Controleert of de persoon eigenaar is van de hond.
# Return (niet print!) True of False.

class Hond:
    def __init__(self, naam:str) -> None:
        self.naam = naam
        self.eigenaar = ""



class Persoon:
    def __init__(self, naam:str) -> None:
        self.naam = naam
        self.honden = []
    
    def koop_hond(self,hond:"Hond")->None:
        self.honden.append(hond)
        hond.eigenaar = self.naam

    def is_eigenaar(self, hond:"Hond")->bool:
        return self.naam == hond.eigenaar
                     







" Via onderstaande code kan je niveau 1 testen. "

hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
persoon_1 = Persoon("Jos")
persoon_2 = Persoon("Jef")

persoon_1.koop_hond(hond_1)
persoon_2.koop_hond(hond_2)

print(persoon_1.is_eigenaar(hond_1)) # True
print(persoon_2.is_eigenaar(hond_1)) # False


" Via onderstaande code kan je niveau 2 testen. "

# hond_1 = Hond("Lulu")
# hond_2 = Hond("Floris")
# persoon_1 = Persoon("Jos")
# persoon_2 = Persoon("Jef")

# persoon_1.koop_hond(hond_1)
# persoon_2.koop_hond(hond_2)
# persoon_2.koop_hond(hond_1) # Lulu heeft reeds Jos als eigenaar.

# print(persoon_1.is_eigenaar(hond_1)) # True
# print(persoon_2.is_eigenaar(hond_1)) # False

