from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class SignUpForm(FlaskForm):
    firstname = StringField("First Name", [
        validators.InputRequired()
    ])
    lastname = StringField("Last Name", [
        validators.InputRequired()
    ])
    email = EmailField('Email', [validators.InputRequired()])

    username = StringField("User name", [validators.InputRequired(),
                                         validators.Length(max = 25)])

    password = PasswordField('New Password,', [
        validators.InputRequired(),
        validators.EqualTo('check', message = 'Passwords must match'),
        validators.Length(min=4, max=25)
    ])

    check = PasswordField("Repeat Password")


class LoginForm(FlaskForm):
    username = StringField('Username', [
        validators.InputRequired(),
        validators.Length(max = 25)
    ])

    password = PasswordField('Password',[
        validators.InputRequired(),
        validators.Length(min=4, max=25)
    ])
