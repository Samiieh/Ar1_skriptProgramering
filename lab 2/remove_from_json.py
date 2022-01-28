import csv
import json

def remove_person():
    
    with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
        lista = json.load(fil) 
        print("Skriv in användarnamnet på personen du vill ta bort")
        an = input("användarnamn: ")
        
        for count, i in enumerate(lista):
            if i["användarnamn"] == an:
                lista.pop(count)
                break
        
    with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
        json.dump(lista, fil, ensure_ascii=False, indent=4)
        print("Updated JSON with deleted person")








    # with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
    #     lista = json.load(fil) 
    #     del lista["h21daekh"]
        
        
    # with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
    #     json.dump(lista, fil, ensure_ascii=False, indent=4)
    #     print("Updated JSON with deleted person")
        
#person = dict(användarnamn=an, förnamn=fn, efternamn=en, epost=ep)
         