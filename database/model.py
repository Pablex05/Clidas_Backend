from .db import db

class ExamenFisicoDensidad(db.Document):
    min = db.FloatField(required=True)
    max = db.FloatField(required=True)