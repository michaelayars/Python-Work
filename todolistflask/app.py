from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#convention is to always create an app instance with a double underscore name

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):  #this creates our data types
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

db.create_all()

#then create a route using a function and the approptiate decorator

@app.get("/") #forward slash indicates home page
def home():
    #todo_list = Todo.query.all()
    todo_list = db.session.query(Todo).all()
    return "Hello World"
    return render_template("base.html", todo_list=todo_list)

#this all uses get commands which isn't ideal

# @app.route("/add", methods=["POST"])  this adds a new item
@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/update/<int:todo_id>") #this updates the app
def update(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/delete/<int:todo_id>") # this deletes items
def delete(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

#to run app - 
#export FLASK_APP=app.py exports environment variables
#export FLASK_ENV=development  this gets hot reloading
#flask run
