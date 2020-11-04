
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField

class BasicForm(FlaskForm):
	Task = StringField('Task description')
	status = SelectField('choice', choices=[('done','done'), ('incomplete','no')])
	submit = SubmitField('Add Task')

