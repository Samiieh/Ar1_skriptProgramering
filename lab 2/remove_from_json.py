import csv
import json


def remove_person():
    
    # Läser in JSON filen
    # Går igenom listan med en forloop, och tittar ifall an input stämmer med key["användarnamn"]
    # isåfall så tas den key'n bort.
    # detta görs genom en while loop, för att få till error hantering, 
    # även mellanslag tas bort med .strip
    # sedan uppdateras json filen med den nya uppdaterade listan
    
    try:
        with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
            lista = json.load(fil) 
            message = "Skriv in användarnamnet på personen du vill ta bort"
            deleted = False
        
            while not deleted:         #
                print(message)
                an = input("användarnamn: ").strip()
                for v, k in enumerate(lista):
                    if k["användarnamn"] == an:
                        lista.pop(v)
                        deleted = True
                    else:
                        message = "Fel användare. Försök igen."
                        
    except FileNotFoundError:
        print('File not found, sure it uses the correct filename?')                        
        
        
        
    with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
        json.dump(lista, fil, ensure_ascii=False, indent=4)
        print("Updated JSON with deleted person")