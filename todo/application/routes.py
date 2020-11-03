from application import app, db
from application.models import Todo
from flask import render_template


@app.route('/')
def main():
	all_todo = Todo.query.all()
	return render_template('main.html', all_todo= all_todo)


@app.route('/add')
def add():
	new_Todo = Todo(description="New Task",status = 'new' )
	db.session.add(new_Todo)
	db.session.commit()
	return "Added new Todo to database"

@app.route('/update/<int:id>/<task>')
def update(id, task):
	first_game = Todo.query.get(id)
	first_game.description = task
	db.session.commit()
	return first_game.description

@app.route('/complete/<int:id>')
def complete(id):
        todo_to_complete = Todo.query.get(id)
        todo_todo_complete.status = 'Complete'
        db.session.commit()
        return "Task changed"

@app.route('/incomplete/<int:id>')
def incomplete(id):
        todo_to_incomplete = Todo.query.get(id)
        todo_todo_complete.status = 'Incomplete'
        db.session.commit()
        return "Task set as incomplete"


@app.route('/delete/<int:id>')
def delete(id):
	todo_to_delete = Todo.query.get(id)
	db.session.delete(todo_to_delete)
	db.session.commit()
	return "Deleted Task"



