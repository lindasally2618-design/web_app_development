# app/models/budget.py
"""Budget model definition for monthly budget settings.
Provides CRUD helper methods.
"""

from datetime import datetime
from .. import db

class Budget(db.Model):
    __tablename__ = 'budget'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))  # NULL for overall budget
    amount = db.Column(db.Float, nullable=False)
    period = db.Column(db.String(20), nullable=False, default='monthly')  # future support: weekly, yearly
    created_at = db.Column(db.String(30), default=lambda: datetime.utcnow().isoformat())

    # Relationships are accessible via backrefs defined in User and Category

    def __repr__(self):
        return f"<Budget user_id={self.user_id} amount={self.amount} period={self.period}>"

    # CRUD helpers
    @staticmethod
    def create(user_id, amount, period='monthly', category_id=None):
        """Create a new budget record.
        Args:
            user_id: Owner user ID.
            amount: Budget amount.
            period: Budget period (default 'monthly').
            category_id: Optional category ID for category‑specific budget.
        """
        budget = Budget(
            user_id=user_id,
            amount=amount,
            period=period,
            category_id=category_id,
        )
        db.session.add(budget)
        db.session.commit()
        return budget

    @staticmethod
    def get_by_id(budget_id):
        return Budget.query.get(budget_id)

    @staticmethod
    def get_all_for_user(user_id):
        return Budget.query.filter_by(user_id=user_id).all()

    def update(self, **kwargs):
        """Update fields of the budget instance.
        Accepts any of the model attributes as keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
