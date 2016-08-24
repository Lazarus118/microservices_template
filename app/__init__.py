from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Register application blueprints
from app.api import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')
