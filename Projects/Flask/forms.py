from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               Length(min=2, max=20)
                           ])

    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=5, max=20)
                             ])
    confirm_password = PasswordField('Confirm Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password')
                             ])
    submit = SubmitField('Sing Up')

class LoginForm(FlaskForm):
# email is used to login bc its easier to rmb, confirm password is not needed
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Email()
                        ])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=5, max=20)
                             ])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')