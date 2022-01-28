import json
import csv


def add_person():

    with open('labb2_personer.json', 'r', encoding="utf-8-sig") as fil:
        add = json.load(fil)
        an = input("Användarnamn: ")
        fn = input("Förnamn: ").title()
        en = input("Efternamn: ").title()
        ep = an + "@du.se"
        person = dict(användarnamn=an, förnamn=fn, efternamn=en, epost=ep)
    
        add.append(person)
        print()
        print("Added person object.")
    
    
#användarnamn;förnamn;efternamn;epost
    with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
        json.dump(add, fil, ensure_ascii=False, indent=4)
        print("Updated JSON with person.")        