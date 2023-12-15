#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ first end point """
    return 'Hello HBNB'


@app.route('/hbnb')
def hbnb():
    """ second  end point """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ display “C ” followed by the value of the text variable """
    text = text.replace("_", " ")
    return f'C {text}'


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>')
def python(text):
    """ display “Python ”, followed by the value of the text variable """
    text = text.replace("_", " ")
    return f'Python {text}'

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
