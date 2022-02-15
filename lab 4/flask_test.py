from flask import Flask, escape, request,jsonify, render_template
import sqlite3
import json

app = Flask(__name__) # skapar en instans av flask där vi skickar in namnet på klassen etc

@app.route('/') # definiera en route, startsidan.
def index():    # skapar en metod för vad som ska hända när man kommer till startsidan
    return render_template('index.html')

@app.route('/postjson/', methods=['POST'])
def postjson():
    data = request.form
    print(data)
    return render_template("user.html", data=data)

@app.route('/weather', methods=['POST'])
def vadsomhelst():
    data = request.json
    print(data)
    
    #test = [data["moist"], data["pressure"], data["temp"], data["orten"]]

    sql = '''INSERT INTO WeatherData (Moist, Pressure, Temp, Plats)
    VALUES
    ({0},{1},{2},"{3}")
    '''.format(data["moist"],data["pressure"],data["temp"],data["orten"])

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    return ""

@app.route('/show/', methods=['GET'])
def show():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM WeatherData''')
    WeatherData = c.fetchall()

    return ""

app.run(host='0.0.0.0', port=5000)


