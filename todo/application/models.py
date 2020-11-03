from application import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(255), nullable = False)
	status = db.Column(db.String(30), nullable = False )

