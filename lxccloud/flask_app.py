from uuid import uuid4

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

from flask_wtf.csrf import CSRFProtect

from lxccloud.settings import DB_URL

from lxccloud.cache import cache

from lxccloud.gui_blueprint import gui_blueprint
from lxccloud.jsapi_blueprint import jsapi_blueprint
from lxccloud.fileio_blueprint import fileioapi_blueprint

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True
app.config["MINIFYHTML"] = False
app.config["SECRET_KEY"] = "super-secret"
app.config["SECURITY_PASSWORD_SALT"] = "super-secret"
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_LOGIN_USER_TEMPLATE"] = "log-in.html"
app.config["SECURITY_REGISTER_USER_TEMPLATE"] = "sign-up.html"
app.config["SECURITY_POST_LOGIN_VIEW"] = "clusters"


cache.init_app(app)

csrf = CSRFProtect(app)

csrf.init_app(app)

db = SQLAlchemy(app)

from lxccloud.models_pgdb import User, Role  # noqa: E402

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

app.register_blueprint(gui_blueprint)
app.register_blueprint(jsapi_blueprint)
app.register_blueprint(fileioapi_blueprint)


@app.before_first_request
def create_user():
    db.create_all()
    if user_datastore.get_user("admin") is None and user_datastore.get_user("user") is None:
        admin_role = user_datastore.find_or_create_role("admin")
        user_role = user_datastore.find_or_create_role("user")

        user_datastore.create_user(email="admin", password="password", uuid=uuid4().hex)  # noqa: E501
        user_datastore.create_user(email="user", password="password", uuid=uuid4().hex)  # noqa: E501

        db.session.commit()

        admin = user_datastore.get_user("admin")
        user_datastore.add_role_to_user(user=admin, role=admin_role)
        user = user_datastore.get_user("user")
        user_datastore.add_role_to_user(user=user, role=user_role)

        db.session.commit()
