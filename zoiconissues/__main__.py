"""
Small runner for development purposes.
"""


from .models import db
from .views import app


db.create_all()
app.run(debug=True)
