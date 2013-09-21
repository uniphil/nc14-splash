#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    splash
    ~~~~~~

    Splash page for NC14

"""

from babel.core import UnknownLocaleError, get_locale_identifier as locale_id
from flask import Flask, request, url_for, redirect, abort, render_template, Markup
from flask.ext.babel import Babel, get_locale


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
        return request.accept_languages.best_match(['en', 'fr'])
        # return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def root():
    lang = get_locale()
    return redirect(url_for('splash', lang=lang))


@app.route('/<lang>/')
def splash(lang):
    return render_template('splash.html', lang=get_locale())


if __name__ == '__main__':
    import os
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc123')
    app.run(debug=True,
            host='0.0.0.0',
            port=os.environ.get('PORT', 5000))
