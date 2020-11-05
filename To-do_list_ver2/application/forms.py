from flask_wtf import FlaskForm
from wtforms import StringFeild, SubmitFeild
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
	task = StringFeild('Task',
		validators=[DataRequired()])

	submit = SubmitField('Add Todo')
