from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)

application.config["SECRET_KEY"] = "de1ec9c6bc343e6995d959526e2a3d93"
application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" #amazon url here, postgres, pgadmin to view
#amplify to deploy - allows for github upload directly to deploy
#headless ui - animations for UI
#pandamensional
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = "signin" #redirects to login if not logged in

from flaskmain import routes
