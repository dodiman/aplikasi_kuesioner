from flask import Flask
from flask_session import Session

from flask_migrate import Migrate

from .extensions import db, bcrypt
from .models.kategori import User
from flask_bcrypt import Bcrypt

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

import os

migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    UPLOAD_FOLDER = 'static/'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    SESSION_TYPE = 'filesystem'

    pengaturan = {
        'SECRET_KEY': 'ini_adalah_contoh_secret_key',
        'UPLOAD_FOLDER': UPLOAD_FOLDER,
        'SESSION_TYPE': SESSION_TYPE,

        'SQLALCHEMY_DATABASE_URI': 'mysql://root:@localhost:3306/aplikasi3',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,

    }

    app.config.from_mapping(pengaturan)

    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)
    
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     # DATABASE=os.path.join(app.instance_path, '')
    # )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # return User.get(user_id)
        return User.query.get(user_id)
    
    bcrypt.init_app(app)

    db.init_app(app)

    # inisialisasi migrasi
    migrate.init_app(app, db)

    from . import aplikasiku, mulai
    app.register_blueprint(aplikasiku.bp)
    app.register_blueprint(mulai.index.bp)
    
    return app