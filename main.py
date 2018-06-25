from flask import Flask

app = Flask(__name__)
PORT= 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "not found"

@app.route('/', methods = ['GET'])
def homepage():
	return "hola conchatumare"

if __name__ == '__main__':
	app.run(port = PORT, debug =DEBUG)