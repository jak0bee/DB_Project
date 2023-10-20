#Marcell Dorkó (6326607)  and Jakub Suszwedyk (6310933)
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


database_url = "mysql+pymysql://admin:Database2023!@database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com/Main"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socket = SocketIO(app)

db = SQLAlchemy(app)
