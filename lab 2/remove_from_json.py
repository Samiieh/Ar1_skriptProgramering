import csv
import json
from multiprocessing.sharedctypes import Value

def remove_person():
    
    
    try:# TRY ME DADDY
        with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
            lista = json.load(fil) 
            message = "Skriv in användarnamnet på personen du vill ta bort"
            deleted = False
        
            while not deleted:
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
        
               


            # if i["användarnamn"] == an: # letar igenom listan och försöker matcha input med ett användarnamn från listan
            #     lista.pop(count)
            #     print("Updated JSON with deleted person")
            #     break



     # i["användarnamn"] != an:
            #     an = input("användarnamnet finns inte med i listan, försök igen. ")
            #     lista.pop(count)
            #     return remove_person()
    
    # with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
    #     lista = json.load(fil) 
    #     del lista["h21daekh"]
        
        
    # with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
    #     json.dump(lista, fil, ensure_ascii=False, indent=4)
    #     print("Updated JSON with deleted person")
        
#person = dict(användarnamn=an, förnamn=fn, efternamn=en, epost=ep)
         