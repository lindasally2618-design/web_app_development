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
        category_id = request.form.get('category_id')
        new_tx = Transaction(
            user_id=current_user.id,
            category_id=int(category_id) if category_id else None,
            amount=float(request.form.get('amount') or 0),
            type=request.form.get('type', 'expense'), 
            note=request.form.get('note', ''),
            date=request.form.get('date', datetime.utcnow().strftime('%Y-%m-%d'))
        )
        db.session.add(new_tx)
        db.session.commit()
        return redirect(url_for('ledger.list_transactions'))
    
    categories = Category.query.filter_by(user_id=current_user.id).all()
    # 如果使用者沒有任何分類，自動幫他建立預設分類
    if not categories:
        default_names = ['飲食', '交通', '購物', '薪資']
        for name in default_names:
            cat = Category(user_id=current_user.id, name=name)
            db.session.add(cat)
        db.session.commit()
        categories = Category.query.filter_by(user_id=current_user.id).all()
        
    return render_template('ledger/add.html', categories=categories)

@ledger_bp.route('/<int:transaction_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    if transaction.user_id != current_user.id:
        return redirect(url_for('ledger.list_transactions'))
        
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        transaction.category_id = int(category_id) if category_id else None
        transaction.amount = float(request.form.get('amount') or transaction.amount)
        transaction.type = request.form.get('type', transaction.type)
        transaction.note = request.form.get('note', transaction.note)
        transaction.date = request.form.get('date', transaction.date)
        db.session.commit()
        return redirect(url_for('ledger.list_transactions'))
        
    categories = Category.query.filter_by(user_id=current_user.id).all()
    return render_template('ledger/edit.html', transaction=transaction, categories=categories)

@ledger_bp.route('/<int:transaction_id>/delete', methods=['POST'])
@login_required
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    if transaction.user_id == current_user.id:
        db.session.delete(transaction)
        db.session.commit()
    return redirect(url_for('ledger.list_transactions'))