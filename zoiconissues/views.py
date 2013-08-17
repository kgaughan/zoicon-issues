"""
View functions.
"""

from flask import request, render_template

from .core import app


@app.route('/')
def overview():
    return render_template('overview.html')


@app.route('/projects')
def projects():
    return ''


@app.route('/issues')
def issues():
    return ''
