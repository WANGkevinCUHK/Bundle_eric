from flask import Flask
from flask_migrate import Migrate
from config import Config
from exts import db
from BP.user_bp import user_bp
from BP.event_bp import event_bp
from BP.friend_bp import friend_bp
from flask_wtf.csrf import CSRFProtect
#csrf = CSRFProtect()

app = Flask(__name__)
#csrf.init_app(app)
app.config.from_object(Config)
db.init_app(app)



migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix="/")
app.register_blueprint(event_bp,url_prefix="/event")
app.register_blueprint(friend_bp,url_prefix="/friend")



if __name__ == '__main__':
    app.run(debug=True)