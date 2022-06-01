from app import app, db
from models import *
from flask import jsonify

@app.route('/clidas')
def index():
    return 'bienvenido a CLIDAS!'

@app.route('/analisis')
def listas_analisis():
    try:
        listaAnalisis = db.session.query(Analisis).all()
        return jsonify(listaAnalisis)
    except:
        return 'Error'

def page_not_found(error):
    return '<h1>Page not found</h1>'