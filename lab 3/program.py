import file_handling
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
        B~~~~~~~~~~~~~~~~~~~~~~~~D ~                                     ~  Ɑ~~~~~~~~~~~~~~~~~~~~~~~~𐐒
        ##############################################################################################
        """)
        # Ber användaren om namnet på en film, sparar detta i searced_movies
        # sedan använder vi searched_movies i url:en till får metod fetch_url
        # skickar med urlen som en parameter till metoden
        # Metoden returnerar sedan requesten till result
        # Om key Search finns i result.keys()
        # Körs en forloop som går in i key Search och skriver ut varje keys för: Titel, År, imdbID.
        # Sedan får användaren ange imdbID på filmen den vill ha mer information om
        # Och då görs ett till anrop till metoden fetch_url, med det nya inputet i url:en istället.
        # Denna gång använder vi ?i istället för ?s som vid första anropet.
        # Metoden returnerar värdet och sparar detta i result som vid tidigare anrop.
        # Vi skickar med result till save_to_json metoden
        #  
        ans=input("Välj ett av alternativen mellan 1 -3: ")
        print()
        if ans=="1":
            searched_movie = input("Skriv in namnet på filmen du vill söka: ") # Ber användaren om namnet på en film, sparar detta i searced_movies
            result = fetch_movie.fetch_url(f'https://www.omdbapi.com/?s={searched_movie}&apikey=8ad4d71&type=movie') #fetch.fetch_url i program-menyn
            
            if "Search" in result.keys(): 
                for k in result["Search"]: # Körs en forloop som går in i key Search och skriver ut varje keys för: Titel, År, imdbID.
                    print("Titel: " + k["Title"])
                    print("År: " + k["Year"])
                    print("imdbID: " + k["imdbID"])
                    print()
                id=input("Ange imdbID på den filmen du söker: ") # Sedan får användaren ange imdbID på filmen den vill ha mer information om
                print()
                # Denna gång använder vi ?i istället för ?s som vid första anropet.
                result = fetch_movie.fetch_url(f'https://www.omdbapi.com/?i={id}&apikey=8ad4d71&type=movie') # Och då görs ett till anrop till metoden fetch_url, med det nya inputet i url:en istället.
                file_handling.save_to_json(result) # Metoden returnerar värdet och sparar detta i result som vid tidigare anrop.
                # Vi skickar med result till save_to_json metoden
                print("Titel: " + result["Title"]) 
                print("År: " + result["Year"])
                print("Plot: " + result["Plot"])
                print()
            else:
                print(f"{searched_movie} Sökningen finns tyvärr inte, testa en annan film! ")
            
        elif ans=="2": # om användaren väljer 2 så laddas json filen och visar de senaste sökningarna
            result = file_handling.load_json_file()
            print("Senaste sökningar: ")
            for movie in result: #En for-loop som printar ut, titel, year, och imdbID.
                print(movie["Title"])
                print(movie["Year"])
                print("imdbID: " + movie["imdbID"])
                print()
            # Här kan användaren välja att få mer information ifall den skriver in imdbID till en film
            svar = input("Ange imdbID på filmen du vill veta mer om: ") 
            print()
            for movie in result: #Ifall träff på imdbID, så printas Titel och Handling ut med en for-loop.
                if movie["imdbID"] == svar:
                    print(movie["Title"])
                    print(movie["Plot"])
        
        elif ans=="3": # Här är användaren tråkig och vill stänga av vårat kära program
            print("Ha en trevlig filmkväll, hejdå!")
            print()
            svar = False
            

                
                
main()