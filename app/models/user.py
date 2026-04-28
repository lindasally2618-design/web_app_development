# app/models/user.py
"""User model definition.
Uses SQLAlchemy ORM. Provides basic CRUD helpers.
"""

from datetime import datetime
from .. import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.String(30), default=lambda: datetime.utcnow().isoformat())

    # Relationships
    categories = db.relationship('Category', backref='user', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', backref='user', cascade='all, delete-orphan')
    budgets = db.relationship('Budget', backref='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User {self.email}>"

    # CRUD helpers
    @staticmethod
    def create(email, password_hash):
        user = User(email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
