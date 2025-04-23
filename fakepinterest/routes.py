from fakepinterest import app, database
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
from fakepinterest.models import Usuario, Foto
from fakepinterest import bcrypt
import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('homepage.html', form=form)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form = FormCriarConta()
    if form.validate_on_submit():
        senha = bcrypt.generate_password_hash(form.senha.data)
        usuario = Usuario(nome_usuario=form.nome_usuario.data, 
                          senha=senha, 
                          email=form.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', id_usuario=usuario.id))
    return render_template('criarconta.html', form=form)

@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form = FormFoto()
        if form.validate_on_submit():
            foto = form.foto.data
            secure_foto = secure_filename(foto.filename)
            caminho_foto = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_foto)
            foto.save(caminho_foto)
            foto = Foto(imagem=secure_foto, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()         
            return redirect(url_for('perfil', id_usuario=current_user.id))
        return render_template('perfil.html', usuario=current_user, form=form)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil.html', usuario=usuario, form=None)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/feed', methods=['GET', 'POST'])
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao.desc()).all()
    return render_template('feed.html', fotos=fotos)