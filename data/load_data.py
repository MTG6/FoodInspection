import requests
import pandas as pd

def load_data():
	"""Load data from City of Chicago API
	
	Load data from JSON, transform to DataFrame, and then fill NA's
	
	Returns a Data Frame
	
	"""
	url_endpoint = 'https://data.cityofchicago.org/resource/cwig-ma7x.json'
	response = requests.get(url_endpoint)
	data = response.json()
	df = pd.DataFrame(data)
	df.violations = df.violations.fillna('')
	
	print(df.columns)
	return df
	
if __name__ == "__main__":
    load_data()