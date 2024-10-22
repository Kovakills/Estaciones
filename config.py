import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para la gestión de sesiones
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    
    # Configuración de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
