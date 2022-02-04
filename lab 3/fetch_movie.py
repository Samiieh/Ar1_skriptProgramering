import requests

# parametern med url:en skickas in till fetch_url och sparas i response
# Sedan görs response om till ett json objekt vi kallar för data_jsonObj
# sedan returneras data_jsonObj tillbaka till program.py
def fetch_url(url):
    
    response = requests.get(url)
    data_jsonObj = response.json()
    return data_jsonObj
    
    
        
# läsa från movies.json och printa