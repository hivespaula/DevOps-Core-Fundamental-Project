#input output to webpage - get post put delete
from application import app, db
from application.models import Characters, Objectives
from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from application.forms import AddCharacter, UpdateCharacter

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = AddCharacter()
    all_characters = Characters.query.all()
    return render_template('add_character.html', form=form, characters=all_characters)

@app.route('/add', methods = ['GET', 'POST'])
def add():
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
        return redirect(url_for('home'))
    return render_template('add_character.html', form=form, character=character)

@app.route('/delete/<int:id>')
def delete(id):
    delete_character = Characters.query.filter_by(id=id).first()
    db.session.delete(delete_character)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    updateform = UpdateCharacter()
    update_character = Characters.query.filter_by(id=id).first()
    if request.method == 'POST':
        if updateform.validate_on_submit():
            update_character.char_name = updateform.name.data
            update_character.lvl = updateform.lvl.data
            update_character.proffesion = updateform.proffesion.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_character.html', form=updateform)