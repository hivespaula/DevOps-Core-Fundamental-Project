#basic application setup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from os import getenv

app = Flask(__name__)
#'mysql+pymysql://user:password@123.45.6.78:3306/mydatabase'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

from application import routes
