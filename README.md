## web introuction


>- not login status
>  - index
>    - login 
>      - login form
>    - register
>      - register form
>- login status
>  - logout
>    - index
>  - event list
>    - each event linking
>      - event details page
>        - register event
>  - add event 
>    - event form
>  - friendlist
>    - friend list page
>  - add friend
>    - add friend form
>  - my info
>    - my info list
>      - my event
>        - withdrawal my event
>      - etc
>    - change my info
>      - change info list



## database introduction

> use: mySQL <br>
> reason:  <br>
> advantage: <br>
> disadvantage: <br>

> solution: <br>
>  - User
>    - id primekey
>    - username
>    - email
>    - createTime
>    - activity_id(foreign key)
>    - activity(foreign key)
>    - friendlist(backref)
>  - Event
>    - id primekey
>    - venue
>    - startTime
>    - description
>    - createTime
>    - crearor_id
>    - participants(backref)
>  - Friendship
>    - id primekey
>    - dst_id
>    - src_id(foreign key)
>    - src(foreign key)


## Flask framework intro

> use: Flask <br>
> reason:  <br>
> advantage: <br>
> disadvantage: <br>

> - app(app server)
> - config (config info)
> - ext(datebase)
> - forms(wtf form checking)
> - models(User Event Friendship)
> - templates(html response)
>   - index etc
>   - register etc
>   - list etc
>   - infomation page etc
> - migration (database migration)
>   - BP(blueprint)
>     - user_bp
>       - index
>       - register
>       - login
>       - logout
>       - info
>       - change
>     - event_bp
>       - event_list
>       - event_create
>       - event_list/id
>       - event_register
>       - event_withdrawl
>     - friend_bp
>       - friend_list
>       - friend_add


## How to use it


>1. download this whole project
>2. create your own PC mySQL server
>3. open config.py and configure it with your own server infomation
>4. make sure your mySQL is connected
>5. in terminal, use "flask db init" "flask db migrate" and "flask db upgrade" one by one
>6. check your own mySQL database, check if the database you choose have the desired forms
>7. run the app.py file
>8. go to http://127.0.0.1:5000 in your chrome or click the linking in the "RUN console"