# app/routes/trabajador.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

trabajador_bp = Blueprint('trabajador', __name__)

@trabajador_bp.route('/reportes')
@login_required
def reportes():
    return render_template('trabajador/reportes.html', username=current_user.username)

@trabajador_bp.route('/perfil')
@login_required
def perfil():
   return render_template('trabajador/perfil.html')


@trabajador_bp.route('/configuracion')
@login_required
def configuracion():
    return render_template('trabajador/configuracion.html', username=current_user.username)

@trabajador_bp.route('/estaciones')
@login_required
def estaciones():
    return render_template('estaciones.html', username=current_user.username)
