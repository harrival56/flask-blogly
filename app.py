"""Blogly application."""

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtention
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "harrison"
app.config['DEBUG_TB_INTERCEPTION_REDIRECT'] = False
debug =DebugToolbarExtention(app)

connect_db(app)
db.create_all()