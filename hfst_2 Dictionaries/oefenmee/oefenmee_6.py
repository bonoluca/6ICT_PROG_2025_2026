
# Start de oefen mee met onderstaande dictionary.


filmscores = {
    "godfather": 9,
    "avatar": 3,
    "oppenheimer": 7.5
}


for index, element in enumerate(filmscores):
    
    print(element)
    print(filmscores[element])

    print(f'de film {element} heeft een score van {filmscores[element]} ')

# Doorloop ieder element apart. Print voor ieder element de zin:
# De film *film* kreeg een score van *score* op 10.

# 	In de opdrachtprompt ziet dit er als volgt uit.
# 	De film godfather kreeg een score van 9 op 10.
# 	De film avatar kreeg een score van 3 op 10.
# 	De film oppenheimer kreeg een score van 7.5 op 10.
