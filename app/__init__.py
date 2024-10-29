from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import Usuario
        return Usuario.query.get(int(user_id))

    # Registrar blueprints
    from app.routes.auth import auth_bp
    from app.routes.estacion_routes import estacion_routes
    from app.routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(estacion_routes)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.route('/')
    def home():
        if current_user.is_authenticated:
            if current_user.role == 'admin':
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('auth.dashboard'))
        else:
            return redirect(url_for('auth.login'))

    return app
