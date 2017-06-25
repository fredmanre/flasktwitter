from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # bd para flask
# manejador de python con multiples llamados[db. runserver, shell]
from flask_script import Manager
# permite migraciones y actualizaciones en la bd
from flask_migrate import Migrate, MigrateCommand
# Para el manejo de sesiones y  remember_me
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Para el manejo del LoginManager
lm = LoginManager()
lm.init_app(app)


from app.models import models
from .controllers import controllers
