from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, BooleanField

# add character form
class AddCharacter(FlaskForm):
    name = StringField('Character Name')
    lvl = IntegerField('Character level')
    proffesion = SelectField('Proffesion', choices=[
        ('Alchemy','Alchemy'), ('Engineering','Engineering'), 
        ('Enchanting', 'Enchanting'), ('Blacksmithing', 'Blacksmithing'),
        ('Inscription','Inscription'), ('Jewelcrafting', 'Jewelcrafting'), 
        ('Leatherworking', 'Leatherworking'), ('Tailoring', 'Tailoring')])
    submit = SubmitField('Add Character')

# quick copy paste of add character 
# has different wording in submit field
class UpdateCharacter(FlaskForm):
    name = StringField('Character Name')
    lvl = IntegerField('Character level')
    proffesion = SelectField('Proffesion', choices=[
        ('Alchemy','Alchemy'), ('Engineering','Engineering'), 
        ('Enchanting', 'Enchanting'), ('Blacksmithing', 'Blacksmithing'),
        ('Inscription','Inscription'), ('Jewelcrafting', 'Jewelcrafting'), 
        ('Leatherworking', 'Leatherworking'), ('Tailoring', 'Tailoring')])
    submit = SubmitField('Update Character')

# objectives form
class ObjectivesForm(FlaskForm):
    daily = BooleanField('Daily quest', default=False)
    weekly = BooleanField('Weekly quest', default=False)
    proffesion = BooleanField('Weekly quest', default=False)