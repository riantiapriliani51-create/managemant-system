from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # admin / user

class Barang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ruang = db.Column(db.String(1))
    nama = db.Column(db.String(100))
    jumlah = db.Column(db.Integer)
    unit = db.Column(db.String(20))
    gambar = db.Column(db.String(100))
    min_qty = db.Column(db.Integer, default=0)
    max_qty = db.Column(db.Integer, default=0)

class LogTransaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pengguna = db.Column(db.String(50))
    tanggal = db.Column(db.String(20))
    jam = db.Column(db.String(10))
    aksi = db.Column(db.String(20))   # Ambil / Tambah
    jumlah = db.Column(db.Integer)
    unit = db.Column(db.String(20))
    jumlah_saat_ini = db.Column(db.Integer)



def init_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

        if Barang.query.count() == 0:
            data_awal = [
                Barang(ruang='A', nama='KABEL FASA', jumlah=10, unit='meter', gambar='Kabel fasa.jpg', min_qty=2, max_qty=10),
                Barang(ruang='A', nama='KABEL NYAF', jumlah=1, unit='roll', gambar='Kabel female to female.jpg', min_qty=2, max_qty=10),
                Barang(ruang='A', nama='JUMPER MALE TO MALE', jumlah=5, unit='pcs', gambar='Kabel Jumper Male to Male.jpg', min_qty=2, max_qty=10),
                Barang(ruang='A', nama='JUMPER MALE TO FEMALE', jumlah=10, unit='pcs', gambar='Kabel male to female.jpg', min_qty=2, max_qty=10),
                Barang(ruang='A', nama='JUMPER FEMALE TO FEMALE', jumlah=15, unit='pcs', gambar='Kabel female to female.jpg', min_qty=2, max_qty=10),
            ]
            db.session.add_all(data_awal)
            db.session.commit()
        # Buat user default jika belum ada
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                password=generate_password_hash('admin123'),
                role='admin'
            )
            db.session.add(admin)

        if not User.query.filter_by(username='user').first():
            user = User(
                username='user',
                password=generate_password_hash('user123'),
                role='user'
            )
            db.session.add(user)

        db.session.commit()