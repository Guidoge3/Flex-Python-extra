import io

bestand = open("Klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:

    tekst_regel = tekst_regel.strip()
    
    print(tekst_regel)

    tekst_regel = bestand.readline()
