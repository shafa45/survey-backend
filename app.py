from flask import Flask, request
import pyrebase
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID"),
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route('/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        data = request.get_json()
        db.child("config-table").push(data)
        return 'Success', 200
    else:  # GET
        data = db.child("config-table").get()
        if data.val() is None:
            return 'No data', 404
        else:
            return list(data.val().values())[-1]
        

@app.route('/answer', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        data = request.get_json()
        db.child("answer-table").push(data)
        return 'Success', 200
    else:  # GET
        data = db.child("answer-table").get()
        if data.val() is None:
            return 'No data', 404
        else:
            return list(data.val().values())[-1]


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG") or False, host='0.0.0.0')