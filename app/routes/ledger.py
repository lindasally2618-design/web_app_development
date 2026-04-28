from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models.transaction import Transaction
from app.models.category import Category
from app import db
from datetime import datetime

ledger_bp = Blueprint('ledger', __name__, url_prefix='/ledger')

@ledger_bp.route('/')
@login_required
def list_transactions():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('ledger/list.html', transactions=transactions)

@ledger_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        new_tx = Transaction(
            user_id=current_user.id,
            category_id=None, # 暫時設為 None
            amount=float(request.form.get('amount') or 0),
            type=request.form.get('type', 'expense'), 
            note=request.form.get('note', ''),
            date=datetime.utcnow()
        )
        db.session.add(new_tx)
        db.session.commit()
        return redirect(url_for('ledger.list_transactions'))
    
    return render_template('ledger/add.html')