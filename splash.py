#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    splash
    ~~~~~~

    Splash page for NC14

"""

from babel.core import get_locale_identifier as locale_id
from flask import Flask, request, url_for, redirect, abort, render_template, Markup, flash
from flask.ext.babel import Babel


app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%%'
app.jinja_env.line_comment_prefix = '##'

app.config.update(BABEL_DEFAULT_LOCALE='en_CA',
                  BABEL_DEFAULT_TIMEZONE='UTC')


babel = Babel(app)


@babel.localeselector
def get_locale():
    if request.path.startswith('/en/'):
        return 'en'
    elif request.path.startswith('/fr/'):
        return 'fr'
    else:
        return 'en' # return request.accept_languages.best_match(['en', 'fr'])
        # return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def root():
    return redirect(url_for('splash', lang='en'))


@app.route('/<lang>/')
def splash(lang):
    return render_template('splash.html', lang=get_locale())

@app.route('/<lang>/sponsors/')
def sponsors(lang):
    return render_template('sponsors.html', lang=lang), 200, {'Content-Type': 'text/html'}

@app.route('/<lang>/', methods=['POST'])
def save_email(lang):
    flash('got that email')
    return redirect(url_for('splash', lang=get_locale()))


def freeze_app():
    from flask_frozen import Freezer
    debugged = app.debug
    app.debug = True
    freezer = Freezer(app)
    freezer.freeze()
    app.debug = debugged


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'freeze':
        freeze_app()
        print 'frozen.'
        sys.exit(0)

    import os
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc123')
    app.run(debug=True,
            host='0.0.0.0',
            port=os.environ.get('PORT', 5000))
