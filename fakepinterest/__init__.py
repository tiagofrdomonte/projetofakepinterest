from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config['SECRET_KEY'] = "b62d477eee8a93580f478de22c7ea7b7"
app.config['UPLOAD_FOLDER'] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()  # 🔹 Correto: Criar a instância primeiro
login_manager.init_app(app)  # 🔹 Importante: Associar ao app Flask
login_manager.login_view = "homepage"  # 🔹 Agora funciona sem erro!


from fakepinterest import routes