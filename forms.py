from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8),
        Regexp('(?=.*[A-Za-z])(?=.*\d)', message="Password must contain at least one letter and one number")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    birth_date = DateField('Birth Date (dd.mm.yyyy)', format='%d.%m.%Y', validators=[DataRequired()])
    accept_tos = BooleanField('I accept the terms of service', validators=[DataRequired()])
    submit = SubmitField('Register')
