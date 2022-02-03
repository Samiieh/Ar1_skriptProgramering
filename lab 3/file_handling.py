import json

def save_to_json(data_jsonObj):
    try:
        lista = load_json_file()
        if lista is not None:
            if len(lista) == 5:
                lista.pop(0)
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
    
    
    
    
    
    # def list_searched():
    
#     for searched in saved:
#         print(searched)


# def remove_person():
    
    
#     try:# TRY ME DADDY
#         with open("labb2_personer.json", "r", encoding="utf-8-sig") as fil:
#             lista = json.load(fil) 
#             message = "Skriv in användarnamnet på personen du vill ta bort"
#             deleted = False
        
#             while not deleted:
#                 print(message)
#                 an = input("användarnamn: ").strip()
#                 for v, k in enumerate(lista):
#                     if k["användarnamn"] == an:
#                         lista.pop(v)
#                         deleted = True
#                     else:
#                         message = "Fel användare. Försök igen."
                        
#     except FileNotFoundError:
#         print('File not found, sure it uses the correct filename?')                        
        
        
        
#     with open('labb2_personer.json', 'w', encoding="utf-8-sig") as fil:
#         json.dump(lista, fil, ensure_ascii=False, indent=4)
#         print("Updated JSON with deleted person")




# import json, requests
# from turtle import end_fill
# from urllib import response


# def fetch_url_json(url):
#     response = requests.get(url)
#     data_jsonObj = response.json()
#     try:
#         with open ('file_str.json', 'w', encoding='utf-8') as fpointer:
#             write_data = json.dumps(data_jsonObj)
#             fpointer.write(write_data)
            
#     except Exception as ferr:
#         print(ferr)
        
# def fetch_url_json_dump(url):
#     response = requests.get(url)
#     json_data = response.json()
#     try:
#         with open ('fil.json', 'w', encoding='utf-8') as fpointer:
#             json.dump(json_data, fpointer)

#     except Exception as ferr:
#         print(ferr)            
            
            
        
# fetch_url_json('https://dog.ceo/api/breeds/image/random')        
#fetch_url_json_dump('https://dog.ceo/api/breeds/image/random')