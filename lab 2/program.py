import json
import csv
from read_from_csv import read_csv
# from save_to_json import save_to_json
from show_json import show_json
from add_to_json import add_person
from remove_from_json import remove_person



def main():
    svar=True
    while svar:
        print("""  
        B======D              Välkommen till            Ɑ======𐐒  
        8~~~~~~~~~~~~~~~~~o         Sam     
        # 1. Cvs till Json
        # 2. Visa Json
        # 3. Lägg till person        &
        # 4. Ta bort person
        # 5. Spara fil
        # 6. Exit / breKK
        B~~~~~~~~~~~~~~~~~~D   Danne's labb 2
        """)
        ans=input("Vad skulle du vilja göra? ")     
        print()
        if ans=="1":
            read_csv()
        elif ans=="2":
            show_json()
        elif ans=="3":
            add_person()
        elif ans=="4":
            remove_person()
        #elif ans=="5":
            #save_        
        #else:
            #svar = False 
           


main()
    
    