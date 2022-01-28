import json
import csv


def save_csv():
    
    
    with open('labb2_personer.json', 'r', encoding="utf-8-sig") as jsonfile:     
        json_data = json.load(jsonfile)
        #headers = json_data[0].keys() # tar keys från index 0 och sparar i headers
        
    with open('labb2_personer.csv', 'w', encoding="utf-8-sig", newline='') as csvfile:
        csv_data = csv.writer(csvfile, delimiter=";")
        count = 0
        
        for character in json_data:
            if count == 0:
                header = character.keys()
                csv_data.writerow(header)
                count += 1
            characters = character.values()
            csv_data.writerow(characters)    
            
    # with open('labb2_personer.csv', 'w', encoding="utf-8-sig", newline='') as fil:
    #     writer = csv.writer(fil)
    #     writer.writerow(headers) # lägger till en rad med keys från header
        
        
    #     for users in json_data:
    #         user_data = users.values()
    #         writer.writerow(user_data) # fyller på rad för rad med values