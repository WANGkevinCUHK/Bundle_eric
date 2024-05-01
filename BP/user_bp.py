from flask import Blueprint, render_template, request, redirect, url_for, session
user_bp = Blueprint("user_bp", __name__, url_prefix="/")
from forms import registerForm, loginForm
from models import User, Friendship
from exts import db

@user_bp.route('/')
def index():
    if session.get('user_id'):
        return render_template('user_loginIndex.html')
    else:
        return render_template('user_notloginIndex.html')

@user_bp.route('/info')
def info():
    user = User.query.get(session['user_id'])
    return render_template('user_detail.html', user=user)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('user_register.html')
    else:
        form = registerForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user_bp.login"))
        else:
            print(form.errors)
            return redirect(url_for("user_bp.register"))

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("user_login.html")
    else:
        form = loginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if not user:
                print("email not found")
                return redirect(url_for("user_bp.login"))
            if user.password == password:
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("password wrong")
                return redirect(url_for("user_bp.login"))
        else:
            print(form.errors)
            return redirect(url_for("user_bp.login"))

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@user_bp.route('/change', methods=['GET', 'POST'])
def change():
    if request.method == 'GET':
        return render_template('user_change.html')
    else:
        form = registerForm(request.form)
        if form.validate():
            user = User.query.get(session['user_id'])
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user.email = email
            user.username = username
            user.password = password
            db.session.commit()
            session.clear()
            return redirect(url_for("user_bp.login"))
        else:
            print(form.errors)
            return redirect(url_for("user_bp.change"))


@user_bp.route('/delete')
def delete():
    user = User.query.get(session['user_id'])
    print(session['user_id'])
    print(user)
    for eventParticipant in user.eventList:
        db.session.delete(eventParticipant)
    for event in user.createList:
        db.session.delete(event)
    for friendship in user.friendList:
        dst_id = friendship.dst
        dst = User.query.get(dst_id)
        src = friendship.src
        friendship_rev = Friendship.query.filter_by(dst=src.id,src=dst).first()
        db.session.delete(friendship)
        db.session.delete(friendship_rev)
    db.session.commit()
    db.session.delete(user)
    db.session.commit()
    session.clear()
    return redirect(url_for("user_bp.index"))


