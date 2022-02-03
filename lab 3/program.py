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
        ans=input("Välj ett av alternativen mellan 1 -3: ")
        print()
        if ans=="1":
            searched_movie = input("Skriv in namnet på filmen du vill söka: ")
            result = fetch_movie.fetch_url(f'https://www.omdbapi.com/?s={searched_movie}&apikey=8ad4d71&type=movie') #fetch.fetch_url i program-menyn
            
            if 'Search' in result.keys():
                for k in result["Search"]:
                    print("Titel: " + k["Title"])
                    #saved.append(k["Title"])
                    print("År: " + k["Year"])
                    #saved.append(k["Year"])
                    print("imdbID: " + k["imdbID"])
                    #saved.append(k["Type"])
                    print()
                id=input("Ange imdbID på den filmen du söker: ")
                print()    
                result = fetch_movie.fetch_url(f'https://www.omdbapi.com/?i={id}&apikey=8ad4d71&type=movie')
                file_handling.save_to_json(result)
                print("Titel: " + result["Title"])
                #saved.append(k["Title"])
                print("År: " + result["Year"])
                #saved.append(k["Year"])
                print("Plot: " + result["Plot"])
                #saved.append(k["Type"])
                print()
            else:
                print(f"{searched_movie} Sökningen finns tyvärr inte, testa en annan film! ")
            
        elif ans=="2":
            result = file_handling.load_json_file()
            print("Senaste sökningar: ")
            for movie in result:
                print(movie["Title"])
                print(movie["Year"])
                print("imdbID: " + movie["imdbID"])
                print()
            
            svar = input("Ange imdbID på filmen du vill veta mer om: ")
            print()
            for movie in result:
                if movie["imdbID"] == svar:
                    print(movie["Title"])
                    print(movie["Plot"])
            
                
                
main()