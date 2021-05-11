from flask import Flask

application = Flask(__name__)

@application.route('/')
def HelloWorld():
	return "Hello World!"
