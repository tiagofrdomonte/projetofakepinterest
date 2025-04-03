from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario, Foto

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    botao_confirmacao = SubmitField('Entrar')
    
class FormCriarConta(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    usuario = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=3, max=25)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirma Senha', validators=[DataRequired(), EqualTo('senha', message='Senhas devem ser iguais')])
    botao_confirmacao = SubmitField('Criar Conta')
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado.')