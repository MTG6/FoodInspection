from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return 'This is the melon homepage'

@app.route('/melons')
def melons():
	return 'My favorite melons are: Watermelon, Cantelope, HoneyDew, and MountainDew'	

@app.route('/melons/<melonname>')
def meloninfo(melonname):
	if melonname.lower() not in ('watermelon', 'cantelope', 'honeydew', 'mountaindew'):
		res = '%s is not a melon!!' % melonname
	else:
		res= ' %s is a very fancy melon' % melonname
	return render_template("profile.html",output1=res)

	
if __name__ == "__main__":
	app.run(debug=True)