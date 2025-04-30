from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = False

    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)

    from .auth import auth
    from .routes import api

    app.register_blueprint(auth, url_prefix='/api/auth')
    app.register_blueprint(api, url_prefix='/api')

    return app
