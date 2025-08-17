# Cria a estrutura do banco de dados
from sqlalchemy.orm import backref

from indicadores import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome_usuario = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    companhias = database.relationship('Companhia', backref='usuario', lazy=True)

class Companhia(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome_companhia = database.Column(database.String, nullable=False)
    setor = database.Column(database.String, nullable=False)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)