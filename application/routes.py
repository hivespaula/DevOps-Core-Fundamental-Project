#input output to webpage - get post put delete
from application import app, db
from application.models import Characters, Objectives
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    return render_template('index.html')
