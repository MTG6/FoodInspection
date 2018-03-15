from data import load_data as ld
from data import feature_creation as fc
from app import app , db
from flask import Flask
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine
from develop import train_model as tm
import sqlite3
import pandas as pd
from app.config import SQLALCHEMY_DATABASE_URI

if __name__ == "__main__":
	
	
	# Import and clean data drame
	df = ld.load_data()
	df_f = fc.feature_creation(df)
	
	
	# Load data into AWS connection
	# uri ='mysql+pymysql://mtg6:p&&ssF4!L@foodinspection-db.c9hebod1wl2a.us-west-2.rds.amazonaws.com:3306/foodinspectiondatabase' 
	uri = SQLALCHEMY_DATABASE_URI
	conn = sqlalchemy.engine.create_engine(uri)
	df_f.to_sql("CleanInspections",conn, if_exists="replace")
	print(len(pd.read_sql_query("select * from CleanInspections",conn)))
	
	# Pickle model
	tm.train_model(pd.read_sql_query("select * from CleanInspections",conn))
