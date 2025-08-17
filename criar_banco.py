from indicadores import app, database
from indicadores.models import Usuario, Companhia

with app.app_context():      # cria contexto exigido pelas novas versões do flask
    database.create_all()    # função para criar banco de dados