from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('/Users/matthewgallagher/MSiA/Winter_2018/MSIA_423/FoodInspection/Model.pickle','rb'))

#Homepage
@app.route('/')
def index():
	res = 'This is the Food Inspection homepage'
	return render_template("profile.html" , output1=res)

#Submit user form, store data for predict
@app.route('/addRestaurant', methods=['POST'])
def addRestaurant():
	
	#Store inputs for prediction
	minor=request.form['m_infracs']
	serious=request.form['s_infracs']
	critical=request.form['c_infracs']
	zip=request.form['zip']
	risk=request.form['risk']
	type=request.form['type']
	lowrisk = 0 ; medrisk =  0 ; highrisk = 0
	canvas = 0 ; license = 0 ; recent = 0 ; repeat = 0; complaint = 0
	
	#Create agg features
	infracs_total = minor+serious+critical
	if risk == 'low':
		lowrisk = 1
	if risk == 'medium':
		medrisk = 1
	if risk == 'high':
		highrisk = 1
	
	if type == 'canvas':
		canvas = 1
	if type == 'license':
		license = 1
	if type == 'recent':
		recent = 1
	if type == 'repeat':
		repeat = 1
	if type == 'complaint':
		complaint = 1
	
	#Create prediction input
	X = pd.DataFrame({'zip' : zip, 'infracs_total' : infracs_total, 'infracs_minor' : minor, \
	'infracs_serious' : serious, 'infracs_critical' : critical, 'Risk 1 (High)' : highrisk,\
	'Risk 2 (Medium)' : medrisk,  'Risk 3 (Low)' : lowrisk, 'Canvas' : canvas, \
	'License' : license, 'Recent Inspection' : recent, 'itype_re' : repeat, \
	'itype_complaint' : complaint} , index = [1])
	
	#Predict outcome
	outcome = model.predict(X)
	
	return 'Your restaurant prediction is... %s' % outcome
	

if __name__ == "__main__":
	app.run(debug=True)