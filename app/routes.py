from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm
from app.models import User, db


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		password = form.password.data
		username = form.username.data
		user = User.query.filter_by(username=username).first()
		if user is None or not user.check_password(password):
			flash('Invalid username or password')
		return redirect(url_for('index'))
	return render_template('login_page.html', title='Login page', page='Login page', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		username = form.username.data
		firstName = form.firstName.data
		lastName = form.lastName.data
		user = User(username=username, firstName=firstName, lastName=lastName)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('User has been successfuly registered')
	return render_template('registration_page.html', title='Registration page', page='Registration page', form=form)