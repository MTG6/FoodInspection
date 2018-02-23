from data import load_data as ld
from data import feature_creation as fc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlite3

if __name__ == "__main__":
	
	#Set up SQLAlchemy
	app = Flask(__name__)
	app.config.from_envvar('MSIA_SETTINGS', silent=True)
	db = SQLAlchemy(app)
	
	#Create sqlite DB
	#conn = sqlite3.connect("FoodInspect.db")
	#engine = create_engine('mysql+pymysql:///FoodInspect.db')

	#Load data drame
	df = ld.load_data()
	df_f = fc.feature_creation(df)
	
	#Try to create DB
	engine = create_engine('sqlite:////FoodInspect.db')
	df_f.to_sql("Inspections",engine, if_exists="replace")
	


    