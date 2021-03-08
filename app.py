from flask import Flask, render_template
from um import temp
from flask import jsonify
from flask import request
from db import cursor
import sqlite3

app = Flask(__name__)


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route('/sign-in', methods=["post"])
def p():
    with sqlite3.connect("db.db") as conn:
        text = request.form["text"]
        text1 = request.form["text1"]
        print(text, text1)
        conn.execute(f"INSERT INTO users (id, nickname, password, email, city) \
          VALUES ('1', 'obama', '{text1}', '{text}', 'BARAK')");
        conn.commit()
    return render_template('b.html')


@app.route('/')
def hello_world():
    return render_template('d.html')


@app.route('/sign-in')
def log():
    return render_template('b.html', cursor=cursor)


@app.route('/shlyapa-voice')
def shlp():
    return render_template('c.html')


@app.route('/shweather')
def shweather():
    return render_template('a.html', temp=temp)


if __name__ == '__main__':
    app.run()
