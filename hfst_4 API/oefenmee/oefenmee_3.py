import requests, json

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
response_json = response.json()

with open("chucknorris_data.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")


# Het bestand "chucknorris_data.json" is (waarschijnlijk) niet in de 
# folder "oefenmee" van hfst_4 verschenen. Leg uit waarom het bestand
# "bericht_jokeAPI.json" op de huidige locatie staat 
# (en niet in de map van het bestand oefenmee_3.py).
