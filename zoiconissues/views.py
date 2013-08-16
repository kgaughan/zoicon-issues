"""
View functions.
"""

from flask import request, render_template

from .core import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return ''


@app.route('/projects')
def projects():
    return ''


@app.route('/issues')
def issues():
    return ''
