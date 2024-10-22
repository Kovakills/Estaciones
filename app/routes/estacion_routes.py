from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_required
from app.models.estacion import Estacion
from app import db

estacion_routes = Blueprint('estacion_routes', __name__)

# Ruta para mostrar el formulario de agregar estación
@estacion_routes.route('/estaciones/agregar', methods=['GET'])
@login_required
def agregar_estacion_page():
    return render_template('add_estacion.html')

# Ruta para agregar una nueva estación
@estacion_routes.route('/estaciones', methods=['POST'])
@login_required
def agregar_estacion():
    data = request.form
    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')
    estado = data.get('estado')
    observaciones = data.get('observaciones')
    
    if not nombre or not ubicacion or not estado:
        flash('Faltan datos obligatorios', 'danger')
        return redirect(url_for('estacion_routes.agregar_estacion_page'))
    
    nueva_estacion = Estacion(
        nombre=nombre,
        ubicacion=ubicacion,
        estado=estado,
        observaciones=observaciones
    )
    
    db.session.add(nueva_estacion)
    db.session.commit()
    
    flash('Estación agregada exitosamente', 'success')
    return redirect(url_for('auth.dashboard'))

@estacion_routes.route('/estaciones')
@login_required
def listar_estaciones():
    # Obtiene todas las estaciones de la base de datos
    estaciones = Estacion.query.all()
    # Renderiza el template y pasa las estaciones a la vista
    return render_template('estaciones_list.html', estaciones=estaciones)
