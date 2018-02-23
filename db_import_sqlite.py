import sqlalchemy
import sqlite3

def db_import(df_f):
	""" Load clean data into database
	
	Args:
	df_f (DataFrame): DataFrame formatted for database
	
	Returns:
	Log (str): Confimration of database import
	
	"""
	
	#Create DB
	conn = sqlite3.connect("FoodInspect.db")
	c = conn.cursor()
	
	#Import Data
	testdf.to_sql("Inspections",conn, if_exists="replace")
	t = pd.read_sql_query("select * from Inspections limit 5;", conn)
	conn.close()
	
	return t