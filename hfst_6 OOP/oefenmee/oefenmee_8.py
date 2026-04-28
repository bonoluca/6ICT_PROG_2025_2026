# Oefen mee 8
# Maak een klasse Hond met de eigenschappen naam en massa. 
class Hond:
    klein = True

    def __init__(self, naam:str,  massa:float) -> None:
        self.naam = naam
        self.massa = massa
    

    def genereer_paspoort(self) -> str : 
        passpoort = f'Naam : {self.naam} - {self.massa} kg'
        return passpoort


# Schrijf een methode genereer_paspoort(). Deze methode moet niet rekenen, maar een samengestelde tekst returnen: 
# "Naam: *naam* - Gewicht: *massa* kg". 

# Maak een object van Hond aan, roep de methode op en print de teruggegeven tekst.
hond = Hond("Fido", 8)
paspoort = hond.genereer_paspoort()
print(paspoort) # Naam: Fido - Gewicht: 8 kg




# # setup pin 7 & 31 as output
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(31, GPIO.OUT)

# # Turn on pin 7 & 31
# GPIO.output(7, GPIO.HIGH)
# GPIO.output(31, GPIO.HIGH)
