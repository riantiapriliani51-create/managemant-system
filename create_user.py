from test import app
from db import db, User
from werkzeug.security import generate_password_hash

with app.app_context():

    # Cek admin
    if not User.query.filter_by(username="admin").first():
        admin = User(
            username="admin",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)

    # Cek user biasa
    if not User.query.filter_by(username="user").first():
        user = User(
            username="user",
            password=generate_password_hash("user123"),
            role="user"
        )
        db.session.add(user)

    db.session.commit()

print("Admin & User berhasil dibuat (jika belum ada)")