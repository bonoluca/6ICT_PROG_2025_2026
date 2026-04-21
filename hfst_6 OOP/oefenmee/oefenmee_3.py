# Op welke regels print deze code iets?
# Er zal ook een fout ontstaan. Leg uit waarom.

#je hed er niet self. naam gezet
class Kat:
    naam = "Borysz"

    def miauw(self) -> None:
        print(f"{self.naam} zegt miauw")

kater = Kat()
kater.miauw() 

kitten = Kat()
kitten.miauw()