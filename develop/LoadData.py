import requests
import pandas as pd

def load_date(){
	url_endpoint = 'https://data.cityofchicago.org/resource/cwig-ma7x.json'
	response = requests.get(url_endpoint)
	data = response.json()
	df = pd.DataFrame(data)
	df.violations = df.violations.fillna('')
	
	return df
	}