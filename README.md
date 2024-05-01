# back end system introuction

## front words
> This is a back-end system based on flask framework , mysql database. <br>
> I suppose I've achieved all the functionality requested in the pdf. <br>

> Moreover, I add a new function: friend recommendation which is a must for apps like Bundle(I suppose) and many other functions like deletion and linking for afterward developing.

> I enjoyed the process from learning to building the whole system and really hope I can continue doing such a interesting thing with interesting people regardless my role <br>

> Looking forward to hearing that I can join and let's do something different!

## First of all, I will introduce my technology stack selection

#### flask framework
> 1. Easy to study
> > easy to learn, less than half a day to get started, convenient for the team to unify the technology stack 
> 2. Good community support
> > When launching an app or WeChat app, flask has a wealth of libraries that can speed up the development process, such as face recognition, identity authorisation and email verification
> 3. Highly expandable
> > Flask integrates seamlessly with other popular Python libraries and tools, which allows teams to incrementally expand the functionality and performance of their applications as needed.

####  mysql database
> 1. stable and reliable
> > The mysql database is mature and stable, with a lower probability of incompatibility and bugs, preventing the team from getting stuck in the early stages of development.
> 2. Strong eco-support
> > The combination of mysql and flask is stable and easy to use.
> 3. Suitable for social app like bundle
> > Although mysql is a relational database and support for topologies such as friendship and event-participant is that direct, foreign keys and relational tables can be an efficient solution for Bundle

## Secondly, let's go into the framework


### Flask framework intro

#### It's divided into 4 main parts
> index file: app.py <br>
> supporting py file: config.py, exts.py, forms.py, models.py<br>
> BluePrint directory(functions for API) <br>
> templates directory <br>

#### supporting file
> config.py: used to configure app information, specifically, used to configure mysql links <br>
> exts.py: used to introduce the database <br>
> forms.py: define all the forms you may need to fill in and check its validity <br>
> models.py: define all the data structure you will use in the project. Specifically, user, event, eventParticipantion, friendship <br>

#### BluePrint directory
> user_bp.py: User-related routing
> > Implemented: 
> > 1. indexing
> > 2. registration, login, logout
> > 3. change information, delete account
> > 4. display personal information </b>
>
> event_bp.py: Event-relating routing
> > Implemented:
> > 1. list all the event, linking to all the events
> > 2. show details for any event, participant any event
> > 3. from my info page to see the events I created and participanted, withdrawal any event I participanted, delete any event I created.
> 
> friend_bp.py: Friend-relating routing
> > Implemented:
> > 1. listing all my friend
> > 2. delete any friend
> > 3. add any friend
> > 4. look at the friend recommendation and add any of them

#### templates directory
> It is the front-end display of various forms or lists </b>

> 1. Categorised in terms of relevance into users, events, friendships
> 2. Categorised in terms of Functionality into filling, displaying, and navigating.

#### general overview

> - app(app server)
> - config (config info)
> - ext(datebase)
> - forms(wtf form checking)
> - models(User Event Friendship)
> - templates(html response)
>   - user etc
>   - event etc
>   - friend etc
> - migration (database migration)
>   - BP(blueprint)
>     - user_bp
>     - event_bp
>     - friend_bp


## Secondly, let's go into the database
> Create four tables, Users, Events, EventParticipation, and Friendships. 

> The core idea is:
> 1. use association table to make user and event form many-to-many relationship
> 2. use foreign key to make user get friendList and (created) eventList. Thus, event get creator attribute, friendship get source attribute.

#### Each table is described separately below

>  - User
>    - id (prime key)
>    - username
>    - email
>    - createTime
>    - creatlist(backref) (events created by you)
>    - friendlist(backref) (friendships you have)
>    - eventlist(backref) (events you participanted)

>  - Event
>    - id (prime key)
>    - venue
>    - startTime
>    - description
>    - createTime
>    - crearor_id(foreign key)
>    - participants(backref)

>  - EventParticipantion
>    - id (prime key)
>    - event_id (foreign key)
>    - user_id (foreign key)

#### remark
> I'm defining a one-way friendship here to facilitate later expansion into a follow relationship.

>  - Friendship
>    - id primekey
>    - dst_id
>    - src_id(foreign key)

## Thirdly, the webpage linking
#### you may have a try youself
> I define 2 status: login and non-login
> 1. for forms, I use GET to ask you to fill in, POST to check validity and redirect
> 2. for lists, I did not define methods but you may think it as POST

>- not login status
>  - index
>    - login 
>      - login form
>    - register
>      - register form
>- login status
>  - logout
>    - index
>  - my info page
>    - create-eventlist
>      - check the event
>      - delete the event
>    - particpant-eventlist
>      - check the event
>      - withdraw the event
>    - change my infomation 
>    - delete my account
>  - create event 
>    - event form
>  - event list
>    - each event linking
>      - that event details page
>        - participant that event
>  - friend recommendation
>    - list all the recommended friend
>      - add that friend now
>  - add friend
>    - add friend form
>  - friendlist
>    - friend list page
>    - delete such a friend


## Finally, How to use


>1. download this whole project
>2. pip install all the packages required by requirements.txt(you may need other upgrade etc. according to your environment)
>3. create your own PC mySQL server(for local test)
>4. open config.py and configure it with your own server infomation (database name, which port you are using etc.)
>5. make sure your mySQL is connected (you may use many ways to test, but you may don't know if you don't check)
>6. in terminal, use "flask db init" "flask db migrate" and "flask db upgrade" one by one (Note that you only need init once, this is for data migration if the table is changed)
>7. check your own mySQL database, check if the database you choose have the desired forms
>8. run the app.py file
>9. go to http://127.0.0.1:5000 in your chrome or click the linking in the "RUN console"
>10. if still don't work, plz email me. Let's figure out what's wrong~