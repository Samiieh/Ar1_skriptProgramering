import random , requests, time
# importerar random för att kunna få random tal
# importerar time för att kunna bestämma hur många sekunder mellan varje utskrift

def moist(): #
    return random.randint(0 , 101) #skapar randomvärden för moist

def temp():
    return random.randint(-40 , 50)  #skapar randomvärden för temp

def pressure():
    return random.randint(950 , 1051) #skapar randomvärden pressure

def orten(): #städerna - location variabeln som håller städerna.
    location = ["Phuket","Maldiverna","Noppikoski","Miami","Arboga","Himalaya","Dum Dum", "Bluff City", "Ban Krut", "Pappas källare","Fawqking","Bosses utedass","Dildo i Kanada","Nirvara", "Falun", "Hedemora", "Borlänge", "Malmö", "Stockholm", "Gävle"]
    for i in range(len(location)): # en for-loop som går igenom städerna
        index = random.randrange(0, len(location)) # väljer ut random stad
    return location[index] # returnar dom valda städerna


for i in range(0,8): #for-loop som presenterar de 8 städerna som valdes ovan samt values.
    data = {"moist": moist(), "temp": temp(), "pressure": pressure(), "orten": orten()}
    requests.post("http://127.0.0.1:5000/weather", json = data) # postar till weather, sparar som variabel json
    print("Data skickat") # Endast för att vi ska se att något skickats
    time.sleep(3) # 3 skunder mellan varje "uppdatering" / utskrift

