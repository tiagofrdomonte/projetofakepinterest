from fakepinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    senha = database.Column(database.String(120), nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True)
    
    @login_manager.user_loader
    def load_usuario(id_usuario):
        return Usuario.query.get(int(id_usuario))

class Foto(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String(120), nullable=False, default='default.png')
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.now)
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)