from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anantpanthri@localhost:5432/todoapp'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<TODO ID: {self.id}, DESC {self.description}>'


db.create_all()


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
    # db.session.query(Todo)


@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    error=False
    body={}
    try:
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description']=todo.description
    except:
        db.session.rollback()
        error = True
        print(sys.exec_info())

    finally:
        db.session.close()

    if not error:
        return jsonify(body)
