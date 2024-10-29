from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models.estacion import Estacion
from app import db

estacion_bp = Blueprint('estacion', __name__, url_prefix='/estaciones')

@estacion_bp.route('/nueva_estacion', methods=['GET', 'POST'])
@estacion_bp.route('/nueva_estacion/<int:station_id>', methods=['GET', 'POST'])
def nueva_estacion(station_id=None):
    if request.method == 'POST':
        data = request.form

        if station_id is not None:  # Asegúrate de que station_id no sea None
            # Actualizar la estación existente
            estacion = Estacion.query.get(station_id)
            if estacion:
                estacion.nombre = data['nombre']
                estacion.lugar = data['lugar']
                estacion.observaciones = data['observaciones']
                estacion.informacion_planta = data['informacion_planta']
                estacion.informacion_equipos = data['informacion_equipos']
                estacion.coordenadas = data['coordenadas']
                flash('Estación actualizada exitosamente')
        else:
            # Crear una nueva estación
            estacion = Estacion(
                nombre=data['nombre'],
                lugar=data['lugar'],
                observaciones=data['observaciones'],
                informacion_planta=data['informacion_planta'],
                informacion_equipos=data['informacion_equipos'],
                coordenadas=data['coordenadas']
            )
            db.session.add(estacion)
            flash('Estación agregada exitosamente')

        db.session.commit()
        return redirect(url_for('estacion.dashboard'))  # Redirigir al dashboard

    estacion = Estacion.query.get(station_id) if station_id is not None else None
    return render_template('nueva_estacion.html', estacion=estacion)
