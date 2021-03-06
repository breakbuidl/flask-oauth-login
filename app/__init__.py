import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint

app = Flask(__name__)
app.config.from_object('config.' + os.environ.get('FLASK_ENV') + 'Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

google_bp = make_google_blueprint(scope=["profile", "email"],
                                  offline=True,
                                  redirect_url=app.config['REDIRECT_URL'])

app.register_blueprint(google_bp, url_prefix="/login")

from app import routes, models
