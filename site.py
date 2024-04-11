from flask import Flask, render_template
from flask.helpers import url_for
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'proect_ot_timochi_i_iluchu'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/fifth")
def home():
    return render_template("home.html")


@app.route("/forth")
def home_1():
    return render_template("home_1.html")


@app.route("/first")
def home_2():
    return render_template("trip1.html")


@app.route("/second")
def home_3():
    return render_template("jor2.html")


@app.route("/third")
def home_4():
    return render_template("trip3.html")


@app.route("/six")
def home_7():
    return render_template("gome_6.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
