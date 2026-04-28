# app/__init__.py
"""Flask application factory and initialization.
Sets up the Flask app, loads configuration, registers blueprints,
and initializes extensions (SQLAlchemy, Flask-Login, etc.).
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (instance will be bound in create_app)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login_get"

def create_app():
    """Application factory.
    Returns a configured Flask app instance.
    """
    app = Flask(__name__, instance_relative_config=True)
    # Load default config
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-secret-key"),
        SQLALCHEMY_DATABASE_URI="sqlite:///../instance/database.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Initialise extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from .routes import register_routes
    register_routes(app)

    # Simple health check route (optional)
    @app.route('/health')
    def health():
        return "OK", 200

    return app
