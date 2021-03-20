from flask import Flask, render_template
from um import temp
from flask import jsonify
from flask import request
from db import cursor
import sqlite3
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db1.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route('/sign-up', methods=["post"])
def p():
    with sqlite3.connect("db.db") as conn:
        text = request.form["text"]
        text1 = request.form["text1"]
        text2 = request.form["text2"]
        text3 = request.form["text3"]
        conn.execute(f"INSERT INTO users (id, nickname, password, email, city) \
          VALUES ('{random.randint(1, 10000)}', '{text2}', '{text1}', '{text}', '{text3}')")
        conn.commit()
    return render_template('b.html')


@app.route('/')
def hello_world():
    return render_template('d.html')


@app.route('/sign-up')
def log():
    return render_template('b.html', cursor=cursor)


@app.route('/log-in')
def login():
    return render_template('f.html', cursor=cursor)


@app.route('/shlyapa-voice')
def shlp():
    return render_template('c.html')


@app.route('/shweather')
def shweather():
    return render_template('a.html', temp=temp)


@app.route('/secret')
def a():
    return render_template('h.html', temp=temp)


@app.route('/spb')
def v():
    return render_template('spb_more.html', temp=temp)


@app.route('/msk')
def g():
    return render_template('moscow_more.html', temp=temp)


@app.route('/don')
def h():
    return render_template('donbass_more.html', temp=temp)


if __name__ == '__main__':
    app.run()
