from flask import Flask, render_template, request, redirect, url_for,jsonify
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://xavier:python@localhost:5432/todoapp"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)



class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean,default=False)

    def __str__(self):
        return f"description={self.description}, completed={self.completed}"
    


# Todo.query.delete()

# db.session.commit()
# todo = Todo(description="todo 1")

# db.session.add(todo)
# db.session.commit()

# todos = Todo.query.all()
# print(todos)


@app.route("/")
def home():
    
    print(Todo.query.all())
    
    return render_template("index.html",data=Todo.query.order_by(Todo.id).all())


@app.route("/create" , methods=["post"])
def create():
    description = request.form["description"]
    print(description)
    new_todo = Todo(description=description)
    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/completed/<int:id>")
def completed(id):
    todo = Todo.query.get(id)
    print("-------------------------------",todo)
    todo.completed= not (todo.completed)
    db.session.commit()
    return jsonify({"completed" : todo.completed })


@app.route("/remove/<int:id>")
def remove(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify("True")