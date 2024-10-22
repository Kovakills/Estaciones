from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Verificar si el usuario tiene el rol de 'admin'
    if current_user.role != 'admin':
        return "No tienes permisos para acceder a esta página.", 403
    return render_template('admin_dashboard.html')
