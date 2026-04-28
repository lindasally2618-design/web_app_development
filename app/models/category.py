# app/models/category.py
"""Category model definition for custom tags.
Provides CRUD helpers.
"""

from datetime import datetime
from .user import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(20))
    created_at = db.Column(db.String(30), default=lambda: datetime.utcnow().isoformat())

    # Relationships
    transactions = db.relationship('Transaction', backref='category', cascade='all, delete-orphan')
    budgets = db.relationship('Budget', backref='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Category {self.name}>"

    # CRUD helpers
    @staticmethod
    def create(user_id, name, color=None):
        cat = Category(user_id=user_id, name=name, color=color)
        db.session.add(cat)
        db.session.commit()
        return cat

    @staticmethod
    def get_by_id(cat_id):
        return Category.query.get(cat_id)

    @staticmethod
    def get_all_for_user(user_id):
        return Category.query.filter_by(user_id=user_id).all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
