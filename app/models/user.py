from flask_login import UserMixin
from app import db

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='worker')  # Rol: 'worker' por defecto

    def __init__(self, username, password, role='worker'):
        self.username = username
        self.password = password
        self.role = role
