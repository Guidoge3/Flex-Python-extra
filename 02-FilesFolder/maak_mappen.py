import os
import io
# Bestand in read-only (r) mode openen (wel zo veilig, we gaan niets overschrijven)
bestand = open("klasgenoten.txt", "r")

 

# Eerste regel inlezen en opslaan in de variabele: tekst_regel
tekst_regel = bestand.readline()

 

# while loop gaat door zolang er iets in de variabele tekst_regel staat
while tekst_regel:
    # Let op: laat de code in de while loop 4 spaties inspringen!

 

     # De newline er af halen
     tekst_regel = tekst_regel.strip()

     # De regel op het scherm zetten:
     os.mkdir(tekst_regel)

     # Volgende regel ophalen, zodat de while loop doorgaat
     tekst_regel = bestand.readline()
