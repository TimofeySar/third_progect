from flask import Flask, render_template
from flask.helpers import url_for
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'proect_ot_timochi_i_iluchu'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365)

@app.route("/")
def home():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
