from flask import Flask,render_template
from data import empdata
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

data = empdata()

@app.route('/empdata/')
def emp():	
	return render_template('empdata.html',data1=data)	

if(__name__=='__main__'):
	app.run(debug=True)	