import json

def save_to_json(data_jsonObj):
    try:
        lista = load_json_file()
        if lista is not None:    # om listan inte är None
            if len(lista) == 5:  # om listan har 5 sökningar i sig
                lista.pop(0)     # tar bort den "äldsta" sökningen i listan, den första.
            lista.append(data_jsonObj) # uppdaterar listan utan den äldsta sökningen
        else: # om listan inte finns, så skapas en tom lista och sparar data_jsonObj
            lista = []
            lista.append(data_jsonObj)

        # Öppnar json filen med write, dumpar listan till write_data 
        # skriver sedan till write_data till movies.json
        with open("movies.json", "w", encoding="utf-8") as fpointer:
            write_data = json.dumps(lista, indent=4, ensure_ascii=False)
            fpointer.write(write_data) 
            
    except FileNotFoundError as ferr: #fel-hantering
        print(ferr)
        
        
    
    
def load_json_file(): 
    # öpper json filen med read, laddar in innehålet i en lista och returnerar den
    try:
        
        with open("movies.json", "r", encoding="utf-8-sig") as fil:
            lista = json.load(fil)
            return lista
    except FileNotFoundError: #fel-hantering
        return None