from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
        app = Flask(__name__)

        # App configuration
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_password@localhost:13112/saramin_data'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['JWT_SECRET_KEY'] = 'your_secret_key'

        # Initialize extensions
        db.init_app(app)
        jwt.init_app(app)

        # Register routes
        from .routes import main_bp
        from .auth import auth_bp
        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)

        return app
