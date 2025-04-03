from fakepinterest import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    senha = database.Column(database.String(120), nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    pass

class Foto(database.Model):
    
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(120), nullable=False, default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now)
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)
    pass