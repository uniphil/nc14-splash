#!/usr/bin/env python2

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def splash():
    return "splashy"


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'abc123'
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
