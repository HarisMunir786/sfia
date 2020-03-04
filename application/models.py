#from application import db
#from application import login_manager
#from flask_login import UserMixin

#class Books(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	genre = db.Column(db.String(30), nullable=False)
#	author = db.Column(db.String(30), nullable=False)
#	title = db.Column(db.String(100), nullable=False, unique=True)
#	content = db.Column(db.String(500), nullable=False, unique=True)
#	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#	def __repr__(self):
#		return ''.join([
#			'Genre: ', self.genre, '\r\n',
#			'Author: ', self.author, '\r\n',
#			'Title: ', self.title, '\r\n',
#			'Content: ', self.content
#			])

#class User(db.Model, UserMixin):
#	id = db.Column(db.Integer, primary_key=True)
#	name = db.Column(db.String(100), nullable=False)
#	email = db.Column(db.String(100), nullable=False)
#	password = db.Column(db.String(500), nullable=False)
#	feedback = db.Column(db.String(100), nullable=False)
#	book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

#	def __repr__(self):
#		return ''.join([
#			'Name: ', self.name, '\r\n',
#			'Email: ', self.email, '\r\n',
#			'Feedback: ', self.feedback
#			])

