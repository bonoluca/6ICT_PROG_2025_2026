# Werk verder met de klasse Hond van oefen mee 2.

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




" Via onderstaande code kan je niveau 1 testen. "
hond = Hond("Tico", 1, 13, "jack russel")
print( hond.naam )
hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond("kico", 13, 13, "jack russel")
print( dier.massa )
dier.weegschaal()