import json
import csv


def add_person():

    try:
        with open('labb2_personer.json', 'r', encoding="utf-8-sig") as fil:
            add = json.load(fil)
            while True:
                an = input("Användarnamn: ").strip()
                if an == "":
                    print("Skriv in ett användarnamn: ")
                else:
                    break
            while True:
                fn = input("Förnamn: ").title().strip()
                if fn == "":
                    print("Skriv in ett förnamn: ")
                else:
                    break
            while True:
                en = input("Efternamn: ").title().strip()
                if en == "":
                    print("Skriv in ett efternamn: ")
                else:
                    break            
            # fn = input("Förnamn: ").title().strip()
            # en = input("Efternamn: ").title().strip()
            ep = an + "@du.se"
            person = dict(användarnamn=an, förnamn=fn, efternamn=en, epost=ep) # sparar input i en dict kallad person
    
            add.append(person) # lägger till dict som heter person
            print()
            print("Added person object.")
    except FileNotFoundError:
              print("File not found, sure it uses the correct filename?")
    
#användarnamn;förnamn;efternamn;epost
    with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
        json.dump(add, fil, ensure_ascii=False, indent=4)
        print("Updated JSON with person.")


    