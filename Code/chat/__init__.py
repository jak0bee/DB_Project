from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database_actions import database_url


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
