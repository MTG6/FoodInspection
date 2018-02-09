from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return 'This is the Food Inspection homepage'

@app.route('/UserInformation')
def melons():
	return 'Please enter your restuarant type.'	

@app.route('/UserInformation/<restype>')
def meloninfo(restype):
	if restype.lower() not in ('italian', 'mexican', 'barbacue', 'sushi'):
		res = '%s YOU FAIL !!' % melonname
	else:
		res= 'A %s restuarant should pass.' % restype
	return render_template("profile.html",output1=res)

	
if __name__ == "__main__":
	app.run(debug=True)