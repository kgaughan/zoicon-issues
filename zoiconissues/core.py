"""
Basic configuration and core objects.
"""

import flask


# Default config.
DEBUG = False
SECRET_KEY = 'DEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEFDEADBEEF'

# Application setup.
app = flask.Flask('zoiconissues')
app.config.from_object(__name__)
app.config.from_envvar('ZOICON_ISSUES_SETTINGS', silent=True)
