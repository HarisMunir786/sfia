from application import db
from application.models import User, Book

db.drop_all()
db.create_all()
