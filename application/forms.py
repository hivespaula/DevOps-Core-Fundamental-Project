from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, BooleanField

class AddCharacter(FlaskForm):
    name = StringField('Character Name')
    lvl = IntegerField('Character level')
    proffesion = SelectField('Proffesion', choices=[
        ('Alchemy','Alchemy'), ('Engineering','Engineering'), 
        ('Enchanting', 'Enchanting'), ('Blacksmithing', 'Blacksmithing'),
        ('Inscription','Inscription'), ('Jewelcrafting', 'Jewelcrafting'), 
        ('Leatherworking', 'Leatherworking'), ('Tailoring', 'Tailoring')])
    submit = SubmitField('Add Character')

class UpdateCharacter(FlaskForm):
    name = StringField('Character Name')
    lvl = IntegerField('Character level')
    proffesion = SelectField('Proffesion', choices=[
        ('Alchemy','Alchemy'), ('Engineering','Engineering'), 
        ('Enchanting', 'Enchanting'), ('Blacksmithing', 'Blacksmithing'),
        ('Inscription','Inscription'), ('Jewelcrafting', 'Jewelcrafting'), 
        ('Leatherworking', 'Leatherworking'), ('Tailoring', 'Tailoring')])
    submit = SubmitField('Update Character')

class Objectives(FlaskForm):
    daily_quest = BooleanField('Daily quest', default=False)
    weekly_quest = BooleanField('Weekly quest', default=False)