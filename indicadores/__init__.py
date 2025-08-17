# Cria site
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)    # Cria aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulador.db'
app.config['SECRET_KEY'] = '28b19f1e80ad7cd1fce6afd53f64b4a0'

database = SQLAlchemy(app)  # cria variável do banco de dados
bcrypt = Bcrypt(app)      # permite segurança de senhas
login_manager = LoginManager(app) # gerencia logins de uma aplicação
login_manager.login_view = 'homepage'  # direciona usuário para homepage quando entrar em uma página que precisa de login
login_manager.login_message_category = 'info' # padroniza mensagem


from indicadores import routes