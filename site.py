from flask import Flask, redirect, render_template, request, make_response, session
from data import db_session
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from data.users import User
from data.jobs import Jobs
import datetime
from forms.LoginForm import LoginForm
from forms.JobForm import JobForm
from forms.RegistForm import RegistForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'proect_ot_timochi_i_iluchu'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365)
db_session.global_init("db/komments.db")
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def main():
    db_sess = db_session.create_session()
    comm = db_sess.query(Jobs).all()
    return render_template("main.html", jobs=comm)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.email = form.email.data
        user.hashed_password = form.password.data
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=form.remember_me.data)
        return redirect('/')
    return render_template('regist.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
