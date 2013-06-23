"""
View functions.
"""

from flask import request, render_template

from zoiconissues.core import app


@app.route('/')
def index():
    return render_template('index.html')
