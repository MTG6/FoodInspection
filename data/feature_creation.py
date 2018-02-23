import pandas as pd
import re
from sqlalchemy import create_engine

def feature_creation(df):
	""" Take the raw dataframe from import, generate features for analysis
	
	Args: 
	df (DataFrame): DataFrame output from LoadData()
	
	Returns:
	df_f (DataFrame): DataFrame that includes feature generation
	
	"""
	#Define local variables
	i=0 #Counter
	infractions=[] #List of infractions to add to df
	crt = [] #List of critical infractions
	ser = [] #List of serious infractions
	mnr = [] #List of minor infractions
	

	#Isolate infraction Numbers and their bucket
	while i < len(df):
		s = df['violations'][i]
		infracs = re.findall("\d+",str(re.findall("\|\s\d+",s)))
		infrac_count = len([int(i) for i in infracs])
		m_count = len([int(i) for i in infracs if int(i) > 29 and int(i) <71])
		s_count = len([int(i) for i in infracs if int(i) > 14 and int(i) <30])
		c_count = len([int(i) for i in infracs if int(i) > 0 and int(i) <16])
    
		
		infractions.append(infrac_count)
		crt.append(m_count)
		ser.append(s_count)
		mnr.append(m_count)
		i=i+1
	
	#Add infractions to DataFrame
	df['infracs_total']=infractions
	df['infracs_minor']=mnr
	df['infracs_serious']=ser
	df['infracs_critical']=crt
	
	#Remove unnecessary columns
	cols = range(5,len(df.columns)) #Range of columns to include in database
	df_f = df.iloc[:,cols]
	df_f = df_f.drop(['location','violations','address','aka_name'], axis =1)
	
	print(df_f.columns)
	return df_f

if __name__ == "__main__":
    feature_creation()
    
    

    