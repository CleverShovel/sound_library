from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='../templates')
manager = Manager(app)
Bootstrap(app)

from app import routes