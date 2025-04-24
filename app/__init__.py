from flask import Flask
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from app.models import User
from app.filters import filters_bp
from app.routes import posts_bp
from extencions import db
from config import Config

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    crsf = CSRFProtect(app)

    db.init_app(app)

    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import main_bp, auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    app.register_blueprint(filters_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
