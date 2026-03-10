""" BELANGRIJK! Gebruiker venv_AI voor deze oefening. """

""" Oefening 2 (  / 5)
Bekijk de afbeelding 'oefening_2.png' en 'oefening_2_uitkomst.png'.
    1. Laad afbeelding 'oefening_2.png' in en analyseer deze met yolov8m.pt.
    2. Teken een rood kader rond iedere kat & een groen kader rond iedere hond.
       Het kader mag enkel getekend worden als de zekerheid 80% of hoger is.
    3. Teken een blauw kader rond ieder object dat niet aan de voorwaarden van punt 2 voldoet.
De afbeelding 'oefening_2_uitkomst.png' toont hoe de afbeelding eruit zou moeten zien.
Je mag de functie plt_imshow gebruiken om de verwerkte afbeelding te tonen (opslaan is dus niet nodig).
"""
from matplotlib import pyplot as plt
def plt_imshow(titel, afbeelding):
    plt.imshow(afbeelding, cmap='Greys_r')
    plt.title(titel)
    plt.grid(False)
    plt.show()

# STAP 1: inladen afbeelding.
afbeelding = cv2.imread(r'YOLOdataset/Toets/oefening_2.png')
afbeelding = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2RGB)

tekst = 'hallo'

# STAP 2: detecteer objecten & teken rechthoeken.
objecten = yolo(afbeelding, verbose=False)[0]
for object in objecten.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = object
    x1, y1, x2, y2, class_id = int(x1), int(y1), int(x2), int(y2), int(class_id)
    if class_id == 15:
        cv2.rectangle(afbeelding, (x1, y1), (x2,y2), (255,0,0), 2)
        cv2.putText(afbeelding, f"{yolo.names[class_id]}:{round(score,2)}", (x1+5, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2)
    if class_id == 16:
        cv2.rectangle(afbeelding, (x1, y1), (x2,y2), (0,255,0), 2)
        cv2.putText(afbeelding, f"{yolo.names[class_id]}:{round(score,2)}", (x1+5, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), 2)
    if score <= 0.80 :
        cv2.rectangle(afbeelding, (x1, y1), (x2,y2), (0,0,255), 2)
        cv2.putText(afbeelding, f"{yolo.names[class_id]}:{round(score,2)}", (x1+5, y1+30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)

    
# STAP 3: tonen verwerkte afbeelding.
plt_imshow("Verwerkte afbeelding", afbeelding)

    
