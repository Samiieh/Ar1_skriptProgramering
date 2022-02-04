import json

def save_to_json(data_jsonObj):
    try:
        lista = load_json_file()
        if lista is not None: # om listan inte är tom
            if len(lista) == 5: # om listan har 5 sökningar i sig
                lista.pop(0) # tar bort den "äldsta" sökningen i listan, den första.
            lista.append(data_jsonObj)
        else:
            lista = []
            lista.append(data_jsonObj)
        with open("movies.json", "w", encoding="utf-8") as fpointer:
            write_data = json.dumps(lista, indent=4, ensure_ascii=False)
            fpointer.write(write_data)
            
    except FileNotFoundError as ferr:
        print(ferr)
        
        
    
    
def load_json_file():
    try:
        
        with open("movies.json", "r", encoding="utf-8-sig") as fil:
            lista = json.load(fil)
            return lista
    except FileNotFoundError:
        return None