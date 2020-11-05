from flask_wtf import dbFlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from application.models import ToDoList



class TodoCheck:
	def __init__(self, message):
		self.message = message

	def __call__(self, form, field):
		todoList = ToDoList.query.all()
		for todo in todoList:
			if todo.task == field.data:
				raise ValidationError(self.message)

class TodoForm(FlaskForm):
	task = StringField('Task',
		validators=[DataRequired(),
		TodoCheck(message='Task already exists')])

	submit = SubmitField('Add Todo')
