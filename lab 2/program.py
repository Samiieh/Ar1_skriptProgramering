import json
import csv
from read_from_csv import read_csv
from save_to_csv import save_csv
from show_json import show_json
from add_to_json import add_person
from remove_from_json import remove_person


def main():
    svar=True
    while svar:
        print("""  
        ############################## ===>>   Välkommen till   <<=== ###############################
        B==============================D     ~~~    Sam    ~~~    Ɑ=================================𐐒 
        # 1. Läs in Cvs till Json
        # 2. Visa Json
        # 3. Lägg till person                        &
        # 4. Ta bort person
        # 5. Spara Json till Csv
        # 6. Exit / breKK
        B=============================D  ~~~   Danne's labb 2   ~~~  Ɑ===============================𐐒 
        ##############################################################################################
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
        elif ans=="5":
            save_csv()        
        elif ans == "6":
            print("Tack ha en bra dag.")
            print()
            svar = False
        else:
            print("Välj mellan 1-6 i menyn") 
           


main()