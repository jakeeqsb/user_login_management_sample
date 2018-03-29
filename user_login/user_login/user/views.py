from user_login import app, db
from flask import render_template, redirect, url_for, session, request, flash
from .form import LoginForm, SignUpForm
from .models import User


@app.route('/')
def index():
    return 'hello'

@app.route('/login', methods = ("GET", "POST"))
def login():
    form = LoginForm()
    errmsg = None
    if form.validate_on_submit():
        user = User.query.filter_by(
            username = form.username.data,
            password = form.password.data
        ).limit(1)
        if user.count():
            session['username'] = form.username.data
            if 'next' in session:
                next = session.get('next')
                session.pop('next')
                return redirect(next)
            else:
                return redirect(url_for('login_success'))

    return render_template('user/login.html', form = form, error = errmsg)


@app.route('/signup', methods=("GET", "POST"))
def signup():
    form = SignUpForm()
    error = None
    if form.validate_on_submit():
        if signupcondition(form):
            user = User(
                form.firstname.data,
                form.lastname.data,
                form.email.data,
                form.username.data,
                form.password.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('success'))
        else:
            error = "The email and username must be unique"
    return render_template('user/signup.html', form = form, error = error )

def signupcondition(form):
    usersemail = User.query.filter_by(email = form.email.data).limit(1)
    usersname =  User.query.filter_by(username=form.username.data).limit(1)

    if usersemail.count() > 0:
        flash("The email already exists")
        return False
    if usersname.count() > 0:
        flash("The username already exists")
        return False
    return True

@app.route('/success')
def success():
    return 'Signed up complete'


@app.route('/login_success')
def login_success():
    return 'User logedin'