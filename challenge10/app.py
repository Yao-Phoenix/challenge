#!/usr/bin/env python3
from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/challenge',
    SQLALCHEMY_TRACK_MODIFICATIONS=False))

db = SQLAlchemy(app)

class File(db.Model):

    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category')
    content = db.Column(db.Text)

    def __init__(self,  title, create_time, category_id, content):
        self.title = title
        self.create_time = create_time
        self.category_id = category_id
        self.content = content

class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self, name):
        self.name = name

def insert_dates():
    java = Category('java')
    python = Category('python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Jave is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html', files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html', file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
