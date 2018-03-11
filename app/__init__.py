from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# needed by beanstalk
app = Flask(__name__)

# config
app.config.from_envvar('MSIA_SETTINGS', silent=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/matthewgallagher/MSiA/Winter_2018/MSIA_423/FoodInspection/FoodInspect.db'

# Initialize the database
db = SQLAlchemy(app)