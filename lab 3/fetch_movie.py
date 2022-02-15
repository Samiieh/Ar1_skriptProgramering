import requests


def fetch_url(url):
    
    response = requests.get(url) # parametern med url:en skickas in till fetch_url och sparas i response
    data_jsonObj = response.json() # Sedan görs response om till ett json objekt vi kallar för data_jsonObj
    return data_jsonObj # sedan returneras data_jsonObj tillbaka till program.py