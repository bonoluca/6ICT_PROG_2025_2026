import requests

url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
response_json = requests.get(url).json() # Haal JSON uit response.

# Bepaal of de grap uit 1 of 2 delen bestaat.
if ("joke" in response_json):
    print(response_json["joke"])     # De grap
else:
    print(response_json["setup"])    # De setup
    print(response_json["delivery"]) # De punchline


with open(, "w") as fp:
    (response_json, fp)


# Niveau 1
# Schrijf de response weg naar een JSON-bestand kies de naam zelf. Bekijk de structuur ervan. Waarom is het nodig om met de if-else te werken in de code?

