# Inventory Management System

Sistem manajemen inventori berbasis web menggunakan Flask dan SQLAlchemy.

## Fitur

- Login dengan role (Admin & User)
- Manajemen barang dengan inventory tracking
- Log transaksi (Ambil/Tambah barang)
- Export data ke Excel
- Dashboard untuk Admin dan User

## Requirement

- Python 3.7+
- pip

## Setup & Install

### 1. Clone Repository
```bash
git clone <repository-url>
cd new
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Admin & User Account
```bash
python create_user.py
```
Default credentials:
- Username: `admin` | Password: `admin123` (Admin)
- Username: `user` | Password: `user123` (User)

### 5. Run Application
```bash
python test.py
```

Akses aplikasi di: `http://localhost:5000`

## Deploy ke Railway/Heroku

### 1. Siapkan file tambahan

**Procfile** (untuk Railway/Heroku):
```
web: gunicorn test:app
```

### 2. Update requirements.txt
```bash
pip install gunicorn
pip freeze > requirements.txt
```

### 3. Create .env (jangan di-commit)
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### 4. Push ke GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### 5. Deploy ke Railway
1. Buka [railway.app](https://railway.app)
2. Login dengan GitHub
3. Create New Project → Import from GitHub
4. Pilih repository mu
5. Railway akan auto-detect dan deploy

Atau gunakan platform lain seperti:
- **Heroku** (free tier sudah ditutup)
- **Render** (render.com)
- **PythonAnywhere** (pythonanywhere.com)

## Struktur Folder

```
new/
├── test.py              # Main Flask app
├── db.py                # Database models
├── create_user.py       # Script buat user default
├── requirements.txt     # Dependencies
├── README.md           # Documentation ini
├── .gitignore          # Git ignore rules
├── templates/          # HTML templates
├── uploads/            # Upload files (images, css)
└── instance/           # Database & internal files (di-ignore)
```

## Troubleshooting

**Database minta password?**
- Pastikan urutan setup benar (virtual env → install → create_user)

**Port 5000 sudah terpakai?**
```python
# Edit di test.py
app.run(debug=True, port=5001)
```

**Module not found?**
```bash
pip install -r requirements.txt
```

## License

MIT
