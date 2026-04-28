# app/models/transaction.py
"""Transaction model definition for income/expense records.
Provides CRUD helpers.
"""

from datetime import datetime
from .. import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'
    note = db.Column(db.String(255))
    date = db.Column(db.String(30), nullable=False)  # ISO date string
    created_at = db.Column(db.String(30), default=lambda: datetime.utcnow().isoformat())

    def __repr__(self):
        return f"<Transaction {self.id} {self.type} {self.amount}>"

    # CRUD helpers
    @staticmethod
    def create(user_id, amount, type_, date, category_id=None, note=None):
        txn = Transaction(
            user_id=user_id,
            amount=amount,
            type=type_,
            date=date,
            category_id=category_id,
            note=note,
        )
        db.session.add(txn)
        db.session.commit()
        return txn

    @staticmethod
    def get_by_id(txn_id):
        return Transaction.query.get(txn_id)

    @staticmethod
    def get_all_for_user(user_id):
        return Transaction.query.filter_by(user_id=user_id).order_by(Transaction.date.desc()).all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
