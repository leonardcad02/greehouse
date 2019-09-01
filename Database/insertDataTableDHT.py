import sqlite3
import sys
import temperture


conexion = sqlite3.connect('sensorsData.db')
cursor = conexion.cursor()

#funtion to insert data on a table

def add_data (temperature, humidity):
    cursor.execute("INSERT INTO DHT_data values(datetime('now'),(?), (?))",(temperature,humidity))
    conexion.commit()

#call the function to insert data
add_data(temperature.temperature,temperature.humidity)

for row in cursor.execute("SELECT * FROM DHT_data"):
    print(row)
    
#close the database after use
conexion.close()            
