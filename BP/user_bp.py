from flask import Blueprint, render_template, request
user_bp = Blueprint("user_bp", __name__, url_prefix="/")
print(__name__)
from forms import RegistrationForm

# from flask import render_template, redirect, url_for, flash
# from bp import bp
# from forms.user_form import RegistrationForm, LoginForm, UpdateProfileForm
# from models.user import User
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, logout_user, login_required, current_user

@user_bp.route('/')
def index():
        return render_template('index.html')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegistrationForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
            return "success"
        else:
            print(form.errors)
            return "fall"

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = RegistrationForm(request.form)
        if form.validate():
            return "success"
        else:
            print(form.errors)
            return "fall"

