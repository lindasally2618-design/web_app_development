from app import create_app, db
from app.models.user import User
from app.models.transaction import Transaction
from datetime import datetime
app = create_app()
with app.app_context():
    u = User.query.filter_by(email='test@example.com').first()
    try:
        t = Transaction(user_id=u.id, category_id=None, amount=100.0, type='expense', note='Test', date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        print("Success")
    except Exception as e:
        import traceback
        traceback.print_exc()
