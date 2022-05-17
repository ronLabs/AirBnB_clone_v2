#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Returns a text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Returns text passed as a parameter"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<txt>', strict_slashes=False)
def display_py(txt='is cool'):
    """Returns a text passed as param"""
    return 'Python {}'.format(txt.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """Returns a text if n is a number"""
    if n.isnumeric():
        return '{} is a number'.format(n)
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def num_html(n):
    """Returns a text if 'n' is number, gives a 404 otherwise"""
    if not n.isnumeric():
        abort(404)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def num_html_even_odd(n):
    """Renders an HTML if 'n' is number, gives a 404 otherwise"""
    if not n.isnumeric():
        abort(404)

    even_odd = 'odd'
    if (int(n) % 2 == 0):
        even_odd = 'even'
    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
