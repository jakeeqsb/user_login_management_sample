from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import sys,os
sys.path.append(os.path.abspath(".."))

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from .user import views
