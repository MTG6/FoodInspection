from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# needed by beanstalk
app = Flask(__name__)

# config
app.config.from_envvar('MSIA_SETTINGS', silent=True)

# Initialize the database
db = SQLAlchemy(app)