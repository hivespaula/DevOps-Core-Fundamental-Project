#database models
from application import db

#one character can have many objectives

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(30), nullable=False)
    char_lvl = db.Column(db.Integer, nullable=False)
    char_proffesion = db.Column(db.String(30), nullable=False)
    objectives = db.relationship('Objectives', backref='objectivesbr')


class Objectives(db.Model):
    __tablename__ = 'objectives'
    id = db.Column(db.Integer, primary_key=True)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    daily = db.Column(db.Boolean, default=False)
    weekly = db.Column(db.Boolean, default=False)
    proffesion = db.Column(db.Boolean, default=False)
