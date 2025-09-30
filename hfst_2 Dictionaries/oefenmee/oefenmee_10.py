# # Vul eerst aan. Daarna pas uitvoeren!
dictionary = {
    "a": 0, 
    "b": 1, 
    "c": 1, 
    "d": 2, 
    "e": 3
    }

# """ Geef aan wat volgende code print"""
# " Vul aan:  die print  a: 0, b: 1, c: 1, d: 2, e: 3 "
# print(dictionary)

# " Vul aan: die print  a, b , c , d , e  "
# for x in dictionary:
#     print(x)

# " Vul aan: die neemt alle sleutels en zet die in een lijst ['a', 'b', 'c', 'd', 'e'] "
# print( list(dictionary.keys()))

# " Vul aan: die neemt e en vrevangt 3 met 4 " #corectie die print 3 omdat die gaat kijken als e in de dictionairy zit als die er niet inzit dan print die 4 
# print( dictionary.get("e", 4))

# " Vul aan: die neemt alle waarde en zet die in een lijst [0, 1, 1, 2, 3] "
# print( list(dictionary.values()))

# " Vul aan: die gaat q zoeken e als die die vind gaat die de waarde ervan print anders print die 4"
# print( dictionary.get("q", 4))

# " Vul aan: die gaat de dictionary printen sleutle , waarde "
# for x, y in dictionary.items():
#     print(y, x)

# " Vul aan: die print alle waardes uit dus allen 0,1,1,2,3,"
# for x in dictionary.values():
#     print(x)

# " Vul aan: DIE VERWIJDERD C uit de dictonairy en print de waarde ervan uit dus 1"
# print( dictionary.pop("c"))

"Vul aan: die print de dictonairy met de waarde en sleutels in een lijst "
print( list(dictionary.items()) )
