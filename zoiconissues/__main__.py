"""
Small runner for development purposes.
"""


from zoiconissues.models import db
from zoiconissues.views import app


db.create_all()
app.run(debug=True)
