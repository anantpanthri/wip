from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anantpanthri@localhost:5432/example'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Id:{self.id}, Name-->{self.name}>'

db.create_all()
@app.route('/')
def index():
    person=Person.query.first()
    return 'Hello '+person.name+' my friend'
