from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate,MigrateCommand
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config['TESTING'] = True

db = SQLAlchemy(app)

 
bcrypt=Bcrypt(app)

login_manager=LoginManager(app)

login_manager.login_view='users.login_notify'

mail=Mail(app)


from app.users.routes import users
from app.posts.routes import posts
from app.categories.routes import categories

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(categories)
