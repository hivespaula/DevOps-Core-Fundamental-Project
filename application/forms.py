from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, BooleanField

class AddCharacter(FlaskForm):
    name = StringField('Character Name')
    lvl = IntegerField('Character level')
    proffesion = SelectField('Proffesion', choices=[
        ('alch','Alchemy'), ('eng','Engineering'), ('blacksm', 'Blacksmithing'),
        ('inscr','Inscription'), ('jewel', 'Jewelcrafting'), ('leather', 'Leatherworking')])
    submit = SubmitField('Add Character')

class Objectives(FlaskForm):
    daily_quest = BooleanField('Daily quest', default=False)
    weekly_quest = BooleanField('Weekly quest', default=False)