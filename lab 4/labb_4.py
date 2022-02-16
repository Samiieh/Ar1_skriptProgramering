from flask import Flask, escape, request,jsonify, render_template
import sqlite3
import json

app = Flask(__name__) # skapar en instans av flask där vi skickar in namnet på klassen etc

@app.route('/') # definiera en route, startsidan.
def index():    # skapar en metod för vad som ska hända när man kommer till startsidan
    return render_template('index.html')

# Här är formuläret
@app.route('/postjson/', methods=['POST'])
def postjson():
    data = request.form
    print(data)
    return render_template("user.html", data=data)

# Här Postas väder datan in i database.db
@app.route('/weather', methods=['POST'])
def vader():
    data = request.json
    print(data)
    sql = '''INSERT INTO WeatherData (Moist, Pressure, Temp, Plats)
    VALUES
    ({0},{1},{2},"{3}")
    '''.format(data["moist"],data["pressure"],data["temp"],data["orten"])

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    return ""

# denna url ska visa datan som stoppats in i database.db
@app.route('/data') 
def data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM WeatherDATA''')
    data = c.fetchall()
    #return f"{data}"
    #return jsonify(data)
    return render_template("weather.html", data=data)














# @app.route('/test')
# def test():
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute('''SELECT Moist, Pressure, Temp, Plats FROM WeatherDATA''')
#     test = c.fetchall()
#     return render_template("test.html", data=test)

app.run(host='0.0.0.0', port=5000)


