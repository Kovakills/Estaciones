from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models.user import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = Usuario.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            flash("Login exitoso!", "success")
            # Redirigir según el rol del usuario
            if user.role == 'admin':
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('auth.dashboard'))

        flash('Credenciales inválidas. Inténtalo de nuevo.', 'danger')
    
    if current_user.is_authenticated:
        # Redirigir según el rol del usuario ya autenticado
        if current_user.role == 'admin':
            return redirect(url_for('admin.admin_dashboard'))
        else:
            return redirect(url_for('auth.dashboard'))

    return render_template("login.html")

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Bienvenido, {current_user.username}! Este es tu panel de trabajador.'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))
