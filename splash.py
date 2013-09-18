#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    splash
    ~~~~~~

    Splash page for NC14
"""

from babel.core import UnknownLocaleError, get_locale_identifier as locale_id
from flask import Flask, request, url_for, redirect, abort, render_template
from flask.ext.babel import Babel, get_locale


app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%%'
app.jinja_env.line_comment_prefix = '##'

app.config.update(BABEL_DEFAULT_LOCALE='en_CA',
                  BABEL_DEFAULT_TIMEZONE='UTC')


babel = Babel()


# @babel.localeselector
# def get_locale():
#     if request.path.startswith('/en/'):
#         return 'en'
#     elif request.path.startswith('/fr/'):
#         return 'fr'
#     else:
#         return app.config['BABEL_DEFAULT_LOCALE']


def fake_gettext(message):
    return message


@app.route('/')
def root():
    print request.path
    # look at "accept" headers to see if we can pick a best language
    # default to app.config.get('BABEL_DEFAULT_LOCALE')
    lang = 'en'
    return redirect(url_for('splash', lang=lang))


@app.route('/<lang>/')
def splash(lang):
    print request.url
    print request.path
    return render_template('splash.html', _=fake_gettext)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'abc123'
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
