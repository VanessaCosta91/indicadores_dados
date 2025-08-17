# Cria as rotas do site (links)
from flask import render_template, url_for, redirect, flash, request
from indicadores import app, bcrypt, database
from indicadores.forms import FormLogin, FormCriarconta, FormCadastrarCompanhia
from indicadores.models import Usuario, Companhia
from flask_login import login_required, login_user, logout_user, current_user
import random

# Rota (página) homepage, onde vai fazer o login
@app.route('/', methods=['GET', 'POST'])
def homepage():
    '''
    if current_user.is_authenticaded:
        return redirect(url_for('perfil', id_usuario=current_user.id))
    '''
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', id_usuario=current_user.id))
        else:
            flash('E-mail ou senha incorretos', 'danger') # exibe uma mensagem de erro, se quiser
    return render_template('homepage.html', form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])  # Rota/endereço da pagina criar senha
# Função para criar senha
def criarconta():
    '''
    if current_user.is_authenticaded:
        return redirect(url_for('perfil', id_usuario=current_user.id))
    '''
    form_criarconta = FormCriarconta()     # Variável que busca formulário do scrip forms
    if form_criarconta.validate_on_submit():  # lógica para validar submissão do formulário (dados)
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)  # criptografar senha
        usuario = Usuario(nome_usuario=form_criarconta.nome_usuario.data, email=form_criarconta.email.data, senha=senha) # cadastra usuário no banco de dados, conforme preenchimento do formulário criar conta
        database.session.add(usuario)
        database.session.commit() # adiciona usuário ao banco de cados
        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('homepage')) # direciona para página de login
    return render_template('criarconta.html', form=form_criarconta)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('homepage'))

@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) != int(current_user.id):
        flash("Você não tem permissão para acessar este perfil.", "danger")
        return redirect(url_for('homepage'))

    companhias = Companhia.query.filter_by(usuario_id=current_user.id).all()
    return render_template('perfil.html', usuario=current_user, companhias=companhias)

@app.route('/cadastrar_companhias', methods=['GET', 'POST'])
@login_required
def cadastrar_companhias():
    form_companhia = FormCadastrarCompanhia()
    if form_companhia.validate_on_submit():
        nova_companhia = Companhia(nome_companhia=form_companhia.nome_companhia.data, setor=form_companhia.setor.data, usuario_id=current_user.id)
        database.session.add(nova_companhia)
        database.session.commit()
        flash("Companhia cadastrada com sucesso!", "success")
        return redirect(url_for('perfil', id_usuario=current_user.id))
    return render_template('cadastrar_companhias.html', form=form_companhia)

@app.route('/simulador/<int:id_companhia>')
@login_required
def simulador(id_companhia):
    companhia = Companhia.query.get_or_404(id_companhia)  # busca companhia

    if companhia.usuario_id != int(current_user.id):        # Garante que a companhia pertence ao usuário logado
        flash("Você não tem permissão para acessar essa companhia.", "danger")
        return redirect(url_for('perfil', id_usuario=current_user.id))

    receita = round(random.uniform(50000, 200000), 2)
    despesas = round(random.uniform(20000, 100000), 2)
    lucro = receita - despesas

    indicadores = [
        {"nome": "Receita", "valor": receita},
        {"nome": "Despesas", "valor": despesas},
        {"nome": "Lucro", "valor": round(lucro,2)},
    ]

    return render_template('simulador.html', companhia=companhia, indicadores=indicadores)
