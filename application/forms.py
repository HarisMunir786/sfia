from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Book, User

class RegistrationForm(FlaskForm):
	name = StringField('Name',
        	validators = [
			DataRequired()
        	]
    	)

	email = StringField('Email',
		validators = [
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators = [
			DataRequired()
		]
	)

	confirm_password = PasswordField('Confirm Password',
		validators = [
			DataRequired(),
			EqualTo('password')
		]
	)

	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()

		if user:
			raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		]
	)

	password = PasswordField('Password',
		validators=[
			DataRequired()
		]
	)

	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class AddBookForm(FlaskForm):
	genre = StringField('Genre',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	author = StringField('Author',
		validators = [
			DataRequired(),
			Length(min=2, max=30)
		]
	)
	title = StringField('Title',
		validators = [
			DataRequired(),
			Length(min=2, max=100)
		]
	)
	content = StringField('Content',
		validators = [
			DataRequired(),
			Length(min=2, max=1000)
		]
	)
	image = StringField('Content',
		validators = [
			DataRequired(),
			Length(min=2, max=1000)
		]
	)
	submit = SubmitField('Entry!')
