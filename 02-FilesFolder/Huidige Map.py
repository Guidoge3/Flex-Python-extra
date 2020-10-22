import os

werkmap = os.getcwd()

print("De Huidige map is:" + werkmap)

os.mkdir("Een nieuwe map")
os.mkdir("Nog een nieuwe map")

mapnaam = input("Welke naam wil je voor je map?")

lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
     os.mkdir(mapnaam)
     print("De map " + mapnaam + " is gemaakt.")
else:
     print("Je hebt geen naam ingevoerd")

