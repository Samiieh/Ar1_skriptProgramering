import random , requests, time


def moist():
    return random.randint(0 , 101)

def temp():
    return random.randint(-40 , 50)

def pressure():
    return random.randint(950 , 1051)

def orten():
    location = ["Phuket","Maldiverna","Noppikoski","Miami","Arboga","Himalaya","Dum Dum", "Bluff City", "Ban Krut", "Pappas källare","Fawqking","Bosses utedass","Dildo i Kanada","Nirvara"]
    for i in range(len(location)):
        index = random.randrange(0, len(location))
    return location[index]


for i in range(0,8):
    data = {"moist": moist(), "temp": temp(), "pressure": pressure(), "orten": orten()}
    requests.post("http://127.0.0.1:5000/weather", json = data)
    print("Data skickat")
    time.sleep(3)

