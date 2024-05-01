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
    return render_template('friend_list.html', records=friendlist)

@friend_bp.route('/add', methods=['GET', 'POST'])
def add_friends():
    if request.method == 'GET':
        return render_template('friend_add.html')
    else:
        form = addForm(request.form)
        if form.validate():
            email = form.email.data
            dst = User.query.filter_by(email=email).first()
            src = User.query.get(session['user_id'])
            friendship = Friendship.query.filter_by(dst=dst.id,src_id=src.id).first()
            if friendship:
                print("already add")
                return redirect(url_for("user_bp.index"))
            else:
                friendship1 = Friendship(dst=dst.id)
                friendship2 = Friendship(dst=src.id)
                friendship1.src = src
                friendship2.src = dst
                db.session.add(friendship1)
                db.session.add(friendship2)
                db.session.commit()
                return redirect(url_for("user_bp.index"))
        else:
            print(form.errors)
            return redirect(url_for("friend_bp.add_friends"))

@friend_bp.route('/delete/<int:id>')
def delete_friends(id):
        dst = User.query.get(id)
        src = User.query.get(session['user_id'])
        friendship1 = Friendship.query.filter_by(dst=dst.id,src_id=src.id).first()
        friendship2 = Friendship.query.filter_by(dst=src.id, src_id=dst.id).first()
        if friendship1 and friendship2:
            db.session.delete(friendship1)
            db.session.delete(friendship2)
            db.session.commit()
            return redirect(url_for("friend_bp.list_friends"))
        else:
            print("no friend")
            return redirect(url_for("friend_bp.list_friends"))


@friend_bp.route('/recommend')
def friend_recommendation():
    user_id = session['user_id']
    user = User.query.get(user_id)
    friends = user.friendList
    friendlist = []
    for friendship in friends:
        user = User.query.get(friendship.dst)
        if user:
            friendlist.append(user)
    friendfriendlist = []
    commonfriend = []
    for friend in friendlist:
        firendfriends=friend.friendList
        for friendfriendship in firendfriends:
            frienduser = User.query.get(friendfriendship.dst)
            if frienduser.id != user_id:
                friendfriendlist.append(frienduser)
                commonfriend.append(friend)
    return render_template('firend_recommendation.html', records=friendfriendlist, commonfriend=commonfriend)
