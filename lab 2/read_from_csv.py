import csv
import json


def read_csv():
    lines = []  # tom lista
                # LÄSER IN FRÅN CSV OCH SPARAR I EN LISTA
                # Använder en forloop för att spara till den tomma listan
                # SPARAR LISTAN till JSON FIL med writemode
    with open("labb2_personer.csv", "r", encoding="utf-8-sig") as fil:
        reader = csv.DictReader(fil, delimiter = ";")   
        for i in reader:
            lines.append(i)
        
        
    print("\nRead: done.")  


                #SPARAR LISTAN till JSON FIL

    with open ("labb2_personer.json", "w", encoding="utf-8-sig") as fil:
        json.dump(lines, fil, ensure_ascii=False, indent = 4)
    print("\nWrite: done.")