from flask import Blueprint, render_template, request, redirect, url_for, session
event_bp = Blueprint("event_bp", __name__, url_prefix="/event")
from models import User
from models import Event, EventParticipant
from forms import eventForm
from exts import db

@event_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('event_create.html')
    elif request.method == 'POST':
        form = eventForm(request.form)
        if form.validate():
            venue = form.venue.data
            startTime = form.startTime.data
            description = form.description.data
            event = Event(creator_id = session['user_id'], venue = venue,startTime=startTime,description=description)
            db.session.add(event)
            db.session.commit()
            user_id = session['user_id']
            participant_entry = EventParticipant(user_id=user_id, event_id=event.id)
            db.session.add(participant_entry)
            db.session.commit()
            return redirect(url_for("user_bp.index"))
        else:
            print(form.errors)
            return redirect(url_for("event_bp.create"))

@event_bp.route('/list')
def list_events():
    records = Event.query.order_by(Event.startTime).all()
    return render_template('event_list.html', records=records)

@event_bp.route('/list/<int:id>')
def event_details(id):
    event = Event.query.get(id)
    participantList = []
    records = event.participantList
    for eventParticipant in records:
        participantList.append(User.query.get(eventParticipant.user_id))
    return render_template('event_details.html', event=event, participantList=participantList)


@event_bp.route('/register/<int:event_id>')
def event_register(event_id):
    user = User.query.get(session['user_id'])
    eventidList = []
    for eventParticipant in user.eventList:
        eventidList.append(eventParticipant.event_id)
    if event_id in eventidList:
        print("Already In")
        return redirect(url_for("event_bp.list_events"))
    else:
        participant_entry = EventParticipant(user_id=user.id, event_id=event_id)
        db.session.add(participant_entry)
        db.session.commit()
        db.session.commit()
        participantList=[]
        event = Event.query.get(event_id)
        records = event.participantList
        for eventParticipant in records:
            participantList.append(User.query.get(eventParticipant.user_id))
        return render_template('event_registerConfirm.html', event=event, participantList=participantList)
from .user_bp import user_bp


@event_bp.route('/withdrawal/<int:event_id>')
def withdrawal(event_id):
    user = User.query.get(session['user_id'])
    eventidList = []
    for eventParticipant in user.eventList:
        eventidList.append(eventParticipant.event_id)
    if event_id in eventidList:
        eventparticipant = EventParticipant.query.filter_by(user_id=user.id,event_id=event_id).first()
        if eventparticipant:
            db.session.delete(eventparticipant)
            db.session.commit()
            return render_template('event_withdrawl.html')
        else:
            print("NO RECORD")
            return redirect(url_for("user_bp.info"))
    else:
        print("NO RECORD")

        return redirect(url_for("user_bp.info"))

@event_bp.route('/delete/<int:event_id>')
def delete(event_id):
    user = User.query.get(session['user_id'])
    eventidList = []
    for event in user.createList:
        eventidList.append(event.id)
    if event_id in eventidList:
        event = Event.query.get(event_id)
        for eventParticipant in event.participantList:
            db.session.delete(eventParticipant)
        db.session.commit()
        db.session.delete(event)
        db.session.commit()
        return render_template('event_delete.html')
    else:
        print("NO RECORD")
        return redirect(url_for("user_bp.info"))






