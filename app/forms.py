from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', [DataRequired()])
	password = PasswordField('Password',[DataRequired()])
	submit = SubmitField('Login') 

class RegisterForm(FlaskForm):
	
	firstName = StringField('First Name', [DataRequired()])
	lastName = StringField('Last Name', [DataRequired()])
	password = PasswordField('Password', [DataRequired(),EqualTo('confirmPassword', message='Password must match')])
	confirmPassword = PasswordField('Confirm Password', [DataRequired()])
	submit = SubmitField('Register')
	username = StringField('Username', [DataRequired()])
	
	def validate_username(self, username):
		user = User.query.filter_by(username=self.username.data).first()
		if user:
			raise ValidationError('User Exists!')
		

