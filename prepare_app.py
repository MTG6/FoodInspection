from data import load_data as ld
from data import feature_creation as fc
from app import app , db
from flask import Flask
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine
from develop import train_model as tm
import sqlite3
import logging
import pandas as pd
from app.config import SQLALCHEMY_DATABASE_URI

def prepare_app():
	"""This initializes and updates the model and data infrastructure."""

	# Import and clean data drame
	df = ld.load_data()
	df_f = fc.feature_creation(df)
	
	# Create Connection
	uri = SQLALCHEMY_DATABASE_URI
	conn = sqlalchemy.engine.create_engine(uri)
	
	# Find existing Inspection IDs
	idds = pd.read_sql_query("select DISTINCT inspection_id from CleanInspections", conn)
	df_fi = df_f[~df_f.inspection_id.isin(idds.inspection_id)]
	logging.debug(' -- Number of pulled records: %s' , len(df_f))
	logging.debug(' -- Number of new records: %s', len(df_fi))
	
	# Load data into AWS connection
	df_fi.to_sql("CleanInspections",conn, if_exists="append")
	logging.debug(' -- Updated number of inspections: %s', len(pd.read_sql_query("select * from CleanInspections",conn)))
	
	# Pickle model
	tm.train_model(pd.read_sql_query("select * from CleanInspections",conn))


if __name__ == "__main__":
	logging.basicConfig(filename='app_prep.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
	logging.debug(' --- Begin app prep.')
	prepare_app()
	logging.debug(' --- Completed app prep.')