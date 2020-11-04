from flask import Flask, render_template, redirect, url_for
from application import app, db
from application.models import ToDoList

@app.route('/')
def index():
    return render_template('index.html', todoList = ToDoList.query.all())

@app.route('/add')
def add():
    new_task= ToDoList(task='newtask',status=  'new')
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<idNum>')
def complete(idNum):
    task= ToDoList.query.get(idNum)
    task.status= 'complete'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<idNum>')
def incomplete(idNum):
    task= ToDoList.query.get(idNum)
    task.satus= 'incomplete'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<idNum>/<newTask>')
def update(idNum,newTask):
    task= ToDoList.query.get(idNum)
    task.task=newTask
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<idNum>')
def delete(idNum):
    task_1= ToDoList.query.get(idNum)
    db.session.delete(task_1)
    db.session.commit()
    return redirect(url_for('index'))
