# Werk verder met de klasse Hond van oefen mee 4.

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


" Via onderstaande code kan je niveau 2 testen. "
hond_1 = Hond("Kiko",13,13 ,"jack russel" )
hond_2 = Hond("Tico",1,13 ,"jack russel")

hond_1.weegschaal()
hond_2.weegschaal()
