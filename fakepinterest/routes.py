from fakepinterest import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')