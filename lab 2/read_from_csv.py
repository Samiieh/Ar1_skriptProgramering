import csv
import json
from textwrap import indent
def read_csv():
    lines = []
# LÄSER IN FRÅN CSV OCH SPARAR I EN LISTA
    with open("labb2_personer.csv", "r", encoding="utf-8-sig") as fil:
        reader = csv.DictReader(fil, delimiter = ";")   
        for i in reader:
            lines.append(i)
        #return lines
        
    print("\nRead: done.")  


#SPARAR LISTAN till JSON FIL
    with open ("labb2_personer.json", "w", encoding="utf-8-sig") as fil:
        json.dump(lines, fil, ensure_ascii=False, indent = 4)
    print("\nWrite: done.")