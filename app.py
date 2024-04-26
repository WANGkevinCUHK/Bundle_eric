from flask import Flask
from flask_migrate import Migrate
from config import Config
from exts import db
from BP.user_bp import user_bp
from models import User


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)



migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix="/")
#app.register_blueprint(event_bp)




if __name__ == '__main__':
    app.run(debug=True)