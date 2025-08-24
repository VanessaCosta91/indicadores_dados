# Cria formulário do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, Form
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from indicadores.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

class FormCriarconta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nome_usuario = StringField('Nome do Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmar_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email cadastrado, faça Longin para continuar.')

class FormCadastrarCompanhia(FlaskForm):
    nome_companhia = StringField('Nome do Companhia', validators=[DataRequired()])
    setor = StringField('Setor', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Cadastrar companhia')