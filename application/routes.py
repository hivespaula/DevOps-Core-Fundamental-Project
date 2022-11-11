#input output to webpage - get post put delete
from application import app, db
from application.models import Characters, Objectives
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from application.forms import AddCharacter

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = AddCharacter()
    return render_template('index.html', form=form)

# @app.route('/objectives', methods = ['GET'])
# def objectives():
#     objectives = Objectives.query.all()
#     return render_template('index.html', form=form)