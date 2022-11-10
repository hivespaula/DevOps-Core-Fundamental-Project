#input output to webpage - get post put delete
from application import app, db
from application.models import Characters, Objectives
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    return 'Home Page' #render_template('home.html')
