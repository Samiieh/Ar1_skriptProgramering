import json
import requests
import fetch_movie


def main():
    svar=True
    while svar:
        print("""  
        ############################## ===>>   Välkommen till   <<=== ###############################
        B==============================D     ~~~    Sam    ~~~    Ɑ=================================𐐒 
        
        # 1. Sök efter en filmtitel.
        # 2. Visa senaste sökningar.                 &
        # 3. Avsluta / brEKK
        
        B=======================D    ~~~   Danne's mysiga filmhörna   ~~~  Ɑ=========================𐐒
        B~~~~~~~~~~~~~~~~~~~~~~~~D  
        ##############################################################################################
        """)
        ans=input("Vad skulle du vilja göra? ")
        print()
        if ans=="1":
            searched_movie = input("Skriv namnet på filmen du vill söka: ")
            fetch_movie.fetch_url(f'https://www.omdbapi.com/?s={searched_movie}&apikey=8ad4d71') #fetch.fetch_url i program-menyn
            
            
        #elif ans=="2":

        # elif ans == "3":
        #     svar = False
        else:
            print("Välj mellan 1 och 3 tack :)")            
                
main()