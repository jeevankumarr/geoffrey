from flask import Flask
import configparser
import os


config = configparser.ConfigParser()
config.read('../config.ini')
# print(os.getcwd())
# print([item for item in config['DEFAULT']])
# from flask_bootstrap import Bootstrap
# from .nav import nav

app = Flask(__name__)
# Bootstrap(app)
# nav.init_app(app)

app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = config['DEFAULT']['SECRET_KEY']


from ..app import routes