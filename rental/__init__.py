from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.db'

#postgresql://farentaldb_1n03_user:emk3TijQADx3qjRDzNXKim3Nj8rzSdQh@dpg-csanp608fa8c73cquepg-a.oregon-postgres.render.com/farentaldb_1n03
app.config['SECRET_KEY'] = '38686699db8a350e76a19df4'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from rental import routes
