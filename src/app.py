from flask import Flask
import jwt
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


@app.route('/clidas')
def index():
    return 'bienvenido a CLIDAS!'

@app.route('/analisis')
def listas_analisis():
    try:
        pass
    except:
        return 'Error'

def page_not_found(error):
    return '<h1>Page not found</h1>'

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()

