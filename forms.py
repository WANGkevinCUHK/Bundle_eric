from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User

class registerForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="wrong email!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="wrong uernmae!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="wrong password!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="different password")])

    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="same email!")

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Log In')
#
# class UpdateProfileForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     avatar = StringField('Avatar URL', validators=[DataRequired()])
#     submit = SubmitField('Update')