from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models.user import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    # Cerrar sesión automáticamente si ya había un usuario autenticado
    if current_user.is_authenticated:
        logout_user()  # Forzar logout al cargar la página de login

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
    
    return render_template("login.html")

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']  # Obtiene el rol desde el formulario
        
        new_user = Usuario(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

