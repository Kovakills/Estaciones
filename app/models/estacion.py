from app import db

class Estacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    observaciones = db.Column(db.Text, nullable=True)

    def __init__(self, nombre, ubicacion, estado, observaciones=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.estado = estado
        self.observaciones = observaciones
