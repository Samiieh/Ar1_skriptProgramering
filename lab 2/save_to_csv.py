import json
import csv


def save_csv():
    
    # öppnar json filen med read
    # Tar keys från index 0 och sparar i headers

    # Sedan öppnar vi csv filen i writemode för att kunna skriva över 
    # sparar en rad med key från headers
    # sedan har vi en for loop som går igenom json_data och fyller på rad för rad med values.
    
    with open('labb2_personer.json', 'r', encoding="utf-8-sig") as fil:     
        json_data = json.load(fil)
        headers = json_data[0].keys() # tar keys från index 0 och sparar i headers
        
        
    with open('labb2_personer.csv', 'w', encoding="utf-8-sig", newline='') as fil:
        writer = csv.writer(fil, delimiter=";")
        writer.writerow(headers) # lägger till en rad med keys från header
        
        for users in json_data:
            user_data = users.values()
            writer.writerow(user_data) # fyller på rad för rad med values
    print("Save to Csv successful!")    
