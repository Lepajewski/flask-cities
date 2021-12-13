#coding: utf-8

from flask import Flask
from .models import *

def create_app(config):
    app = Flask(__name__, template_folder='../templates')
    app.config['DEBUG'] = True
    app.config.from_pyfile(config)

    #initialization of data base
    database.init(app.config['DBNAME'], host=app.config['DBHOST'],
                user=app.config['DBUSER'], password=app.config['DBPASS'],
                port=app.config['DBPORT'])

    #database.create_table(Cities) #used only once

    from .cities import bp_cities
    app.register_blueprint(bp_cities)

    return app
