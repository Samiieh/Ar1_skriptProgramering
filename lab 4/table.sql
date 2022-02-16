CREATE TABLE IF NOT EXISTS WeatherData (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Plats VARCHAR(30) NOT NULL,
    Moist VARCHAR(10),
    Temp VARCHAR(10),
    Pressure VARCHAR(10),
    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
