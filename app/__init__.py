from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

google_bp = make_google_blueprint(scope=["profile", "email"],
                                  redirect_url='http://localhost:5000/glogin')
app.register_blueprint(google_bp, url_prefix="/login")

from app import routes, models
