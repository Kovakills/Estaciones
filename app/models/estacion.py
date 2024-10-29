# app/models/estacion.py

from app import db

class Estacion(db.Model):
    __tablename__ = 'estaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    lugar = db.Column(db.String(200), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)
    informacion_planta = db.Column(db.String(200), nullable=False)
    informacion_equipos = db.Column(db.String(200), nullable=False)
    coordenadas = db.Column(db.String(100), nullable=True)  # Puedes almacenar como "lat,lon"
    
    def __init__(self, nombre, lugar, observaciones, informacion_planta, informacion_equipos, coordenadas):
        self.nombre = nombre
        self.lugar = lugar
        self.observaciones = observaciones
        self.informacion_planta = informacion_planta
        self.informacion_equipos = informacion_equipos
        self.coordenadas = coordenadas
