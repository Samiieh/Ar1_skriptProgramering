from textwrap import indent
from pkg_resources import ensure_directory
import requests
import json
# spara till movies.json
def fetch_url(url):
    
    response = requests.get(url)
    data_jsonObj = response.json()
    try:
        with open("movies.json", "w", encoding="utf-8") as fpointer:
            write_data = json.dumps(data_jsonObj, indent=4, ensure_ascii=False)
            fpointer.write(write_data)
            
    except FileNotFoundError as ferr:
        print(ferr)
        
        
# läsa från movies.json och printa

def read_json():
    
    
    with open("movies.json", "r", encoding="utf-8-sig") as fil:
        lista = json.load(fil)
        #print(lista)
        for k in lista.items():
            print(k.values())
            
        
        
        
        
read_json()           





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



















            
# searched_movie = input("Skriv namnet på filmen du vill söka: ")
# fetch_url(f'https://www.omdbapi.com/?s={searched_movie}&apikey=8ad4d71') #fetch.fetch_url i program-menyn





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