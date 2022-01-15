from flask import Flask, render_template

METHODS = ['GET', 'POST']
APP = Flask(__name__)
APP.secret_key = b'test'

@APP.route('/')
def index():
    return render_template('index.html')

APP.run(host='localhost', port=5000, debug=True)