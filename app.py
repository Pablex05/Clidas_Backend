from flask import Flask
from database.db import initialize_db
from resources.routes import initialize_routes, initialize_routes
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/database_clidas'}

initialize_db(app)
initialize_routes(api)

app.run(debug=True)