#input output to webpage - get post put delete
from application import app, db
from application.models import Characters, Objectives
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from application.forms import AddCharacter

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = AddCharacter()
    if request.method == 'POST':
        if form.validate_on_submit():
            character = Characters(
                char_name = form.name.data,
                char_lvl = form.lvl.data,
                char_proffesion = form.proffesion.data
            )
            db.session.add(character)
            db.session.commit()
    all_characters = Characters.query.all()
    return render_template('add_character.html', form=form, characters=all_characters)
