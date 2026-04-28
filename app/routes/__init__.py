# app/routes/__init__.py
"""Register all route blueprints with the Flask app."""

from flask import Flask
from .auth import auth_bp
from .ledger import ledger_bp
from .category import category_bp
# Budget and dashboard blueprints will be imported when they exist

def register_routes(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(ledger_bp)
    app.register_blueprint(category_bp)
    # TODO: register other blueprints (budget, dashboard) when added
