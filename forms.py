from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import Email, EqualTo, Length
from models import User
from flask import session

class registerForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="wrong email!")])
    username = wtforms.StringField(validators=[Length(min=2, max=50, message="wrong uernmae!")])
    password = wtforms.StringField(validators=[Length(min=2, max=50, message="wrong password!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="different password")])

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="same email!")

class loginForm(wtforms.Form):
    email= wtforms.StringField(validators=[Email(message="wrong email!")])
    password = wtforms.StringField(validators=[Length(min=2,max=50,message="wrong password!")])



class eventForm(FlaskForm):
    venue = wtforms.StringField(validators=[Length(min=2,max=50,message="wrong venue!")])
    startTime = wtforms.DateTimeField(format='%Y-%m-%dT%H:%M')
    description = wtforms.StringField(validators=[Length(min=2,max=50,message="wrong description!")])

class addForm(FlaskForm):
    email = wtforms.StringField(validators=[Email(message="wrong email!")])

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if not user:
            raise wtforms.ValidationError(message="no such email!")
        if user.id == session['user_id']:
            raise wtforms.ValidationError(message="cannot add you self")
