from flask import Flask, render_template
from um import temp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('d.html')


@app.route('/sing-in')
def log():
    return render_template('b.html')


@app.route('/about-us')
def about():
    return render_template('c.html')


@app.route('/shweather')
def shweather():
    return render_template('a.html', temp=temp)


if __name__ == '__main__':
    app.run()
