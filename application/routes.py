from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import LoginForm, RegistrationForm, AddBookForm

@app.route('/')
@app.route('/home')
def home():
	bookData = Book.query.all()
	return render_template('home.html', title='Home', books=bookData)
#	return render_template('home.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = User(name=form.name.data, email=form.email.data, password=hash_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('login'))
	form = LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('myaccount'))
	return render_template('login.html', title='Login', form=form)

@app.route('/myaccount')
@login_required
def myaccount():
	user = current_user
#	return render_template('myaccount.html', title='Hi %s'%(user.name), uform=UserForm(), user=user)
	return render_template('myaccount.html', title='My Account')

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/addbook", methods=['GET', 'POST'])
@login_required
def addbook():
	form = AddBookForm()
	if request.method == 'POST':
		if current_user.is_authenticated:
			bookentry = Book(genre=form.genre.data, title=form.title.data, author=form.author.data, content=form.content.data)
			db.session.add(bookentry)
			db.session.commit()
			return redirect(url_for('myaccount'))
		else:
			return render_template('register.html', title='Register', form=form)
	else:
		return render_template('addbook.html', form=form)
