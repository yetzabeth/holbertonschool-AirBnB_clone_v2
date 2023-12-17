#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number(n):
    """only id number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """number template"""
    number = "Number: {}".format(n)
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """is odd or even"""
    if (n % 2 == 0):
        number = "Number: {} is even".format(n)
    else:
        number = "Number: {} is odd".format(n)
    return render_template('6-number_odd_or_even.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
