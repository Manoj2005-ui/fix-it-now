from app import app, db  # assuming app.py is your main file

with app.app_context():
    db.create_all()
    print("Database tables created.")