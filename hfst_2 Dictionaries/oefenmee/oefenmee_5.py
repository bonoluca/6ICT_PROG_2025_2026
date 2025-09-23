# Start de oefening met onderstaande code.



# Combineer onderstaande 2 lijsten samen tot een dictionary. Een deel van de code is reeds gegeven.

films = ["godfather", "avatar", "oppenheimer"]
scores = [9, 3, 7.5]

filmscores = {}


for index, film in enumerate(films):
    sleutel = film  # De sleutel is de huidige film.
    waarde = scores[index]  # De waarde is de overeenkomstige score.
    # Gebruik sleutel/waarde om nieuw dict element te maken.
    filmscores[sleutel] = waarde


print(filmscores)




