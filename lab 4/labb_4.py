from flask import Flask, escape, request,jsonify, render_template
import sqlite3
import json

app = Flask(__name__) # skapar en instans av flask

@app.route('/') # definiera en route, startsidan.
def index():    # skapar en metod för vad som ska hända när man kommer till startsidan
    return render_template('index.html') # laddar in Index.html

# Här är formuläret
@app.route('/postjson/', methods=['POST']) # Tar inputen från formuläret och returnar till user.html
def postjson():
    data = request.form # begär data från formuläret och sparar det i variablen data
    print(data) # printar inputen till consolen så vi ser vad som sker
    return render_template("user.html", data=data)  # returnar varibabeln data till user.html

# Här Postas väder datan in i database.db
@app.route('/weather', methods=['POST']) # 
def vader(): # metod som bestämmer vad som händer när man går till /weather
    data = request.json # begär json och sparar det i en variabel som heter data
    print(data) # printar data till consolen så vi ser vad som sker

    # Lägger in våra datavärden i databasen.db
    # moist, pressure, temp och orten.
    sql = '''INSERT INTO WeatherData (Moist, Pressure, Temp, Plats)
    VALUES
    ({0},{1},{2},"{3}")
    '''.format(data["moist"],data["pressure"],data["temp"],data["orten"]) 

    conn = sqlite3.connect('database.db') # skapar en connection till databasen
    c = conn.cursor() # skapar en curson vi kan arbeta med
    c.execute(sql) # använder cursor och verkställer datan från sql
    conn.commit() # connection commit
    return ""

# denna url ska visa datan som stoppats in i database.db
@app.route('/data') # vad som händer när man besöker url data
def data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM WeatherDATA''')
    data = c.fetchall() # tar all data från WeatherData och sparar i variabeln data
    return render_template("weather.html", data=data) #laddar in HTML-template "weather" med datan


app.run(host='0.0.0.0', port=5000) #


