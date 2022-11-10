from application import db
from application.models import Characters, Objectives

db.drop_all()
db.create_all()
