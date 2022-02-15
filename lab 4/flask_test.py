from base64 import encode
from urllib import request
from flask import Flask, escape, request,jsonify, render_template
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__) # skapar en instans av flask där vi skickar in namnet på klassen etc
CORS(app)

@app.route('/') # definiera en route, startsidan.
def index():    # skapar en metod för vad som ska hända när man kommer till startsidan
    return render_template('index.html')

@app.route('/postjson/', methods=['POST'])
def postjson():

    lista = []
    #person = dict(request.json)
    
    lista.append(request.json)
    print(request.json)

    with open("person.json", "w", encoding="utf-8") as fil:
        fil.write(json.dumps(lista, indent=4, ensure_ascii=False))
    return request.json

# def postjson():
#     user_dict = []
#     user_dict = request.json
#     #user_dict = request.json
#     print(request.json)
#     with open('person.json', 'w') as fil:
#         json.dump(user_dict, fil, indent=4, ensure_ascii=False)
#         fil.write(user_dict)
#     return request.json



# @app.route('/postjson/', methods=['POST'])
# def postjson():
#     personer = request.json
#     print(request.json)
#     with open('person.json', 'w') as fil:
#         json.dumps(personer, fil, ensure_ascii=False, indent=4)
#     return request.json

@app.route('/visa/')
def visa():
    with open('person.json', 'r', encoding="utf-8-sig") as fil:
        visa = json.load(fil)
        #print(visa)
    return f'Användare {visa}'


@app.route('/hello/')
def hello():
    name = request.args.get('name', 'world')
    return f'hello {name}'

@app.route('/users/')
def users():
    # conn = sqlite3.connect('database.db') #skapar en anslutning till databasen
    # c = conn.cursor() # skapar en variabel vi kan arbeta med
    # c.execute('''SELECT username, password, id FROM users''')
    # users = c.fetchall() # hämta allt från users
    users = [
        { "username" : "thomas"},
        { "username" : "johanna"}
    ]
    return jsonify(users)





    #return { 'status' : f'Det här är ditt post data: {request.json}' }
    #request.form.get('fname')
    #name = request.args.get("name", "world")
    #return f"hello {name}"

    
