from flask import render_template, flash, redirect, url_for
from app import app, db, lm
from app.models.forms import LoginForm
from flask_login import login_user, logout_user
from app.models.models import User


@lm.user_loader
def load_user(id):
    return User.get(id)


@app.route('/index/<user>')
@app.route('/', defaults={"user": None})
def index(user):
    return render_template('index.html', user=user)


@app.route('/test', defaults={'name': None})
@app.route('/test/<name>')  # #<int:name> solo numeros
def test(name):
    if name:
        print(name, type(name))
        return "Hola %s!" % name
    else:
        return "Hola usuario!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            print(type(user.id), user.password)
            login_user(user)  # no funciona con python3
            return redirect(url_for('index'))
            flash("Login Success")
        else:
            flash("password Invalid")
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out!")
    return redirect(url_for('login'))


@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    i = User('julia', '124', 'julia riza', 'fff@gmail.com')
    db.session.add(i)
    db.session.commit()
    return "Ok!"


@app.route('/query/<query>')
@app.route('/query', defaults={'query': None})
def consulting(query):
    if query:
        r = User.query.filter_by(username=query).first()
        print(r)
        r.name = "Fredmanre"
        r.username = "Freddy"
        r.email = "freddy-link@hotmail.com"
        db.session.add(r)
        db.session.commit()
        return "OK"
    else:
        r = User.query.order_by(User.username).all()
        print(r)
    return render_template('index.html')
