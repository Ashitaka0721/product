from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('main.config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import main.views