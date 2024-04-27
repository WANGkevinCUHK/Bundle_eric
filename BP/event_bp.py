from flask import Blueprint, render_template, request, redirect, url_for, session
event_bp = Blueprint("event_bp", __name__, url_prefix="/event")
from models import User
from models import Event
from forms import eventForm
from exts import db

@event_bp.route('/list')
def list_events():
    records = Event.query.order_by(Event.startTime).all()
    print(records)
    return render_template('listevent.html', records=records)

@event_bp.route('/list/<int:id>')
def event_details(id):
    event = Event.query.get(id)
    return render_template('event_details.html', event=event)

@event_bp.route('/withdrawal')
def withdrawal():
    user = User.query.get(session['user_id'])
    user.activity = None
    db.session.commit()
    return render_template('event_out.html')

@event_bp.route('/register/<int:event_id>')
def event_register(event_id):
    user_id = session['user_id']
    event = Event.query.get(event_id)
    user = User.query.get(user_id)
    user.activity = event
    db.session.commit()
    #if xx
    return render_template('register_ok.html', event=event)

@event_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createevent.html')
    elif request.method == 'POST':
        form = eventForm(request.form)
        if form.validate():
            venue = form.venue.data
            startTime = form.startTime.data
            description = form.description.data
            event = Event(creator_id = session['user_id'], venue = venue,startTime=startTime,description=description)
            db.session.add(event)
            user_id = session['user_id']
            user = User.query.get(user_id)
            user.activity = event
            db.session.commit()
            return redirect(url_for("user_bp.index"))
        else:
            print(form.errors)
            return redirect(url_for("event_bp.create"))

