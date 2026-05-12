# Maak de klasse Hond aan zoals omschreven in oefen mee 9.
import random
locaties = ["living", "tuin", "buren", "keuken"]

class Hond:
    def __init__(self ,naam:str ):
        self.naam = naam
        self.locatie = random.choice(locaties)
    
    def ziet_hond(self, ander_hond:"Hond"):
        if self.locatie == ander_hond.locatie:
            print(f"{self.naam} ziet {ander_hond.naam} in {self.locatie} ")
            self.locatie = random.choice(locaties)
            print(f"{self.naam} is bang en rent naar de {self.locatie}.")
        else :
            print("ze zien elkaar niet")


# " Via onderstaande code kan je niveau 1 testen. "
# hond_1 = Hond("Lulu",   "tuin")
# hond_2 = Hond("Floris", "tuin")
# hond_3 = Hond("Ranger", "keuken")

# hond_1.ziet_hond(hond_2)
# hond_1.ziet_hond(hond_3)


" Via onderstaande code kan je niveau 2 & 3 testen. Opgelet! Resultaat is random. "
" Best print je in __init__ ook de locatie waar iedere hond start, zo kan je de werking makkelijker nagaan. "

hond_1 = Hond("Lulu")
hond_2 = Hond("Floris")
hond_3 = Hond("Ranger")

hond_1.ziet_hond(hond_2)                  
hond_1.ziet_hond(hond_3)   
          
print(hond_1.locatie)   
