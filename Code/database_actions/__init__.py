from flask import Flask
from flask_sqlalchemy import SQLAlchemy


database_url = "mysql+pymysql://admin:Database2023!@database-1.cotjdrp5li6u.eu-north-1.rds.amazonaws.com/Main"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
