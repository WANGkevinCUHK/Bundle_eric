from flask import Blueprint, render_template, request, redirect, url_for, session
friend_bp = Blueprint("friend_bp", __name__, url_prefix="/friend")
from models import User
from models import Friendship
from models import Event
from forms import addForm
from exts import db


@friend_bp.route('/list')
def list_friends():
    user = User.query.get(session['user_id'])
    friends = user.friendList
    friendlist = []
    for friendship in friends:
        user = User.query.get(friendship.dst)
        if user:
            friendlist.append(user)
    print(friends)
    print(friendlist)
    return render_template('listfriend.html', records=friendlist)

@friend_bp.route('/add', methods=['GET', 'POST'])
def add_friends():
    if request.method == 'GET':
        return render_template('addfriend.html')
    else:
        form = addForm(request.form)
        if form.validate():
            email = form.email.data
            dst = User.query.filter_by(email=email).first()
            src = User.query.get(session['user_id'])
            friendship = Friendship(dst=dst.id)
            friendship.src = src
            db.session.add(friendship)
            db.session.commit()
            return redirect(url_for("user_bp.index"))
        else:
            print(form.errors)
            return redirect(url_for("friend_bp.add_friends"))

@friend_bp.route('/recommend')
def friend_recommendation():
        form = addForm(request.form)
        if form.validate():
            email = form.email.data
            dst = User.query.filter_by(email=email).first()
            src = User.query.get(session['user_id'])
            friendship = Friendship(dst=dst.id)
            friendship.src = src
            db.session.add(friendship)
            db.session.commit()
            return render_template('firendrecommendation.html')
