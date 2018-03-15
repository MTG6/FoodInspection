import requests
import pandas as pd

def load_data():
	"""Load data from API(JSON), transform to DataFrame, and then fill NA's.
	Args:
		None
	Returns:
		df (pd.DataFrame): DataFrame of new inspections from API.
	
	"""
	url_endpoint = 'https://data.cityofchicago.org/resource/cwig-ma7x.json'
	response = requests.get(url_endpoint)
	data = response.json()
	df = pd.DataFrame(data)
	df.violations = df.violations.fillna('')
	
	
	return df
	
if __name__ == "__main__":
    load_data()