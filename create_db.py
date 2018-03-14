from data import load_data as ld
from data import feature_creation as fc
from app import app
from flask import Flask
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine
from develop import train_model as tm
import sqlite3
import pandas as pd
import config


if __name__ == "__main__":
	
	#Set up SQLAlchemy
	#app = Flask(__name__)
	#app.config.from_envvar('MSIA_SETTINGS', silent=True)
	#db = SQLAlchemy(app)
	
	#Create sqlite DB
	#conn = sqlite3.connect("FoodInspect.db")
	#engine = create_engine('mysql+pymysql:///FoodInspect.db')

	#Load data drame
	df = ld.load_data()
	df_f = fc.feature_creation(df)
	
	#Pickle
	#tm.train_model(df_f)
	
	
	#Try to create DB
	#engine = create_engine('sqlite:////Users/matthewgallagher/MSiA/Winter_2018/MSIA_423/FoodInspection/FoodInspect.db')
	#conn = engine.connect()
	#df_f.to_sql("Inspections",conn, if_exists="replace")
	#print(pd.read_sql_query("select * from Inspections limit 5;", conn).columns)
	
	#AWS CONNECTION
	#uri ='mysql+pymysql://mtg6:p&&ssF4!L@foodinspection-db.c9hebod1wl2a.us-west-2.rds.amazonaws.com:3306/foodinspectiondatabase' 
        uri = config.SQLALCHEMY_DATABASE_URI
	conn = sqlalchemy.engine.create_engine(uri)
	df_f.to_sql("CleanInspections",conn, if_exists="replace")
        #pd.read_sql_query("select * from CleanInspections limit 5;",conn)
