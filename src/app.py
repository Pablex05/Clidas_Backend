from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
load_dotenv(override=True)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + os.getenv('DB_USERNAME') + ':' + os.getenv('DB_PASS') + '@localhost/database_clidas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Run server
if __name__ == "__main__":
    from url import *
    from models import *
    app.run(port=os.getenv('PORT'),debug=True)

