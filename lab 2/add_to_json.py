import json
import csv


def add_person():

    # Öppnar json filen i read till en variabel kallad add
    # kör en while loop för att hantera error
    # strippar bort onödiga mellanslag samt gör stor bokstav på förnamn och efternamn
    # Tillåter inte att man kan lämna input tomt
    # sparar input i en dictionairy som heter person
    # sedan sparas person till add som vi läste json filen till
    # Sedan gör vi en json dump för att skriva över json filen med den nya datan

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
            ep = an + "@du.se"
            person = dict(användarnamn=an, förnamn=fn, efternamn=en, epost=ep) # sparar input i en dict kallad person
    
            add.append(person) # lägger till dict som heter person
            print()
            print("Added person object.")
    except FileNotFoundError:
            print("File not found, sure it uses the correct filename?")
    
    with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
        json.dump(add, fil, ensure_ascii=False, indent=4)
        print("Updated JSON with person.")