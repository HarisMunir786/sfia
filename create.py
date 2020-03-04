from application import db
from application.models import Books, User

db.drop_all()
db.create_all()
