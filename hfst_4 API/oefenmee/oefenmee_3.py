

import requests, json, os

# API URL
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_json = response.json()

# Correct pad
folder_path = "hfst_4/oefenmee"
file_path = os.path.join(folder_path, "chucknorris_data.json")  #maak een variabelen aan voor het maken van het pat

# Maak map aan als die niet bestaat
os.makedirs(folder_path, exist_ok=True)

# Schrijf JSON naar bestand
with open(file_path, "w") as fp:
    json.dump(response_json, fp)  #file phat
    print("Data gedumpt!")

# Print de joke
print("Chuck Norris joke:", response_json["value"])


# Het bestand "chucknorris_data.json" is (waarschijnlijk) niet in de folder "oefenmee" van hfst_4 verschenen. 
# Leg uit waarom het bestand "bericht_jokeAPI.json" op de huidige locatie staat 
# (en niet in de map van het bestand oefenmee_3.py).

'omdat je een bestand opent genaamd chucknorris data json'

# Niveau 2
# Pas de code op regel 7 aan. 
# Zorg ervoor dat het bestand "chucknorris_data.json" verschijnt in de folder "oefenmee" van hfst_4.
# 	Tip! Je moet het pad van "chucknorris_data.json" wijzigen. Dit door de string aan te passen.
#         Dit werkt hetzelfde als paden van afbeelding tijdens de lessen van Pygame / websites.

# Voer de code uit om te controleren dat het pad correct is.

