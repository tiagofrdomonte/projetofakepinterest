from fakepinterest import app
from flask import render_template
from flask_login import login_required
from flask_login import current_user
from fakepinterest.forms import FormLogin, FormCriarConta

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form_login = FormLogin()
    return render_template('homepage.html', form=form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta()
    return render_template('criarconta.html', form=form_criarconta)

@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html')