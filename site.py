from flask import Flask, render_template
from flask.helpers import url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/action')
def another_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)