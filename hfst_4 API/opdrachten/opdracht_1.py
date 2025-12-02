""" Voorbeelden (API geeft enkel Engelse zinnen terug):

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""

import requests , json 

query = input("Topic for advice: ")
response_json = requests.get(f"https://api.adviceslip.com/advice/search/{query}").json()

with open (r"6ICT_PROG_2025_2026\hfst_4 API\opdrachten\opdrachten.json", "w") as fp:
    json.dump(response_json, fp)
    print("Data gedumpt!")

print(response_json["slips"][0]["advice"] )

