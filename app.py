"""Adopt application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "SUPER-SECRET-KEY"

debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def landing_page():
    """landing page redirecting to list of all users"""
    return render_template('/templates/base.html')
