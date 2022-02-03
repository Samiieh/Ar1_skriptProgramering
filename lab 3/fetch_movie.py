import requests


def fetch_url(url):
    
    response = requests.get(url)
    data_jsonObj = response.json()
    return data_jsonObj
    
    
        
# läsa från movies.json och printa