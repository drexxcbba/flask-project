from logging import debug
from flask import Flask
from flask.globals import request
from flask.helpers import make_response
from flask import redirect
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/bad')
def bad():
    return '<h1>Bad Request</h1>', 400

@app.route('/cookie')
def cookie():
    response_one = make_response('<h1>This document carries a cookie!</h1>')
    response_one.set_cookie('answer', '42')
    return response_one

@app.route('/redi')
def redi():
    return redirect('http://localhost:5000/user/user_redirected')

if __name__ == '__main__':
    app.run(debug=True)