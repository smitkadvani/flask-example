from flask import Flask

application = Flask(__name__)

@application.route('/')
def HelloWorld():
	return "HelloWorld"

if __name__=='__main__':
	application.run(port=5001)
