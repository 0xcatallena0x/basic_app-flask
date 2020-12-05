from app import db
from app import bcrypt
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(21), unique=True, nullable=False)
	firstName = db.Column(db.String(21), nullable=False)
	lastName = db.Column(db.String(21), nullable=False)
	password_hash = db.Column(db.String(16), nullable=False)

	def set_password(self, password):
		self.password_hash = bcrypt.generate_password_hash(password)

	def check_password(self, password):
		return bcrypt.check_password_hash(self.password_hash, password)
