from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return 'This is the homepage'
	
	
if __name__ == "__main__":
	app.run(debug=True)