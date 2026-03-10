""" BELANGRIJK! Gebruiker venv_AI voor deze oefening. """

""" Oefening 1 (  / 5)
Bekijk de afbeeldingen 'oefening_1.png' en 'oefening_1_uitkomst.png'.
    1. Laad afbeelding 'oefening_1.png' in.
    2. Bewerk deze afbeelding zodat deze er ongeveer uitziet als 'oefening_1_uitkomst.png'.
    3. Sla het resultaat van je bewerking op naar de afbeelding 'oefening_1_resultaat.png'.
"""

import cv2
import os
from matplotlib import pyplot as plt

folder_pad    = r"YOLOdataset"
folder_inhoud = os.listdir(folder_pad) 

#functie om afbeelding weer te geven
def plt_imshow(titel, afbeelding):
    plt.imshow(afbeelding, cmap='Greys_r')
    plt.title(titel)
    plt.grid(False)
    plt.show()


# Afbeelding inladen.
afbeelding_ster = cv2.imread(r"YOLOdataset/Toets/oefening_1.png")

afbeelding_sterGrijs = cv2.cvtColor(afbeelding_ster, cv2.COLOR_BGR2GRAY)

# Afbeelding & pixelwaarden tonen.
plt_imshow("grijsafbeelding", afbeelding_sterGrijs)
cv2.imwrite("YOLOdataset/Toets/oefening_1_resultaat.png",afbeelding_sterGrijs )


