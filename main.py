from flask import Flask, jsonify
from datetime import date
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to API Exploration</p>"

@app.route("/favNumber/<int:n>")
def favNumber(n):
    result = {
        "My Favourite Number" : n
    }
    return jsonify(result)

@app.route("/dateToday")
def dateToday():
    result = {
        "Today's Date" : date.today().strftime("%B %d, %Y")
    }
    return jsonify(result)

@app.route("/getContacts")
def getContacts():
    cnxn = mysql.connector.connect(
    user='explore_user@explore-01',
    password='1qweASD!', 
    host='explore-01.mysql.database.azure.com', 
    database='exploreDataBase')
    cursor = cnxn.cursor()
    query = 'SELECT * FROM Contacts'
    cursor.execute(query)
    result = cursor.fetchall()
    cnxn.close()
    return jsonify(result)



if __name__ == "__main__":
    app.run()
