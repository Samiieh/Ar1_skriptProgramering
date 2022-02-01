import json
import csv
    
#VISA JSON FIL
def show_json():
       
       try:    
              with open ("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
                     test = json.load(fil)
              
                     for i in test:
                            print(i)
       except FileNotFoundError:
              print("File not found, sure it uses the correct filename?")
              
print("\nPrint: done.")
       