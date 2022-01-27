import json
import csv
    
#VISA JSON FIL
def show_json():
           
       with open ("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
              test = json.load(fil)
              for i in test:
                    print(i)
       
       print("\nPrint: done.")