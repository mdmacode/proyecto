
from flask import Flask, request
from flask import render_template

import os
import sys

from prueba2 import sumare
sys.path.append( 'nuevex/')
print( sys.path)
from nuevex import escribirletra

app = Flask(__name__)
PORT= 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "not found"

@app.route('/', methods = ['GET', 'POST'])
def homepage():
	suma = sumare(1 , 2)
	print('***')
	print(suma)
	print('***')
	escribir()
	return render_template('index.html')

@app.route('/subir-foto', methods = ['GET', 'POST'])
def subir_foto():
	if request.method == 'POST':
		user= request.form['user']
		password = request.form['password']
		print(user)
		return render_template('subir-foto.html', user = user, password = password)

	return render_template('index.html')

if __name__ == '__main__':
	app.run(port = PORT, debug =DEBUG)