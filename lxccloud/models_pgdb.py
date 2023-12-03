from flask_security import UserMixin, RoleMixin
from sqlalchemy_utils import JSONType

from lxccloud.flask_app import db


roles_users = db.Table(
    "roles_users", db.Column("user_id", db.Integer(), db.ForeignKey("user.id")), db.Column("role_id", db.Integer(), db.ForeignKey("role.id"))
)


class Cluster(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    uuid = db.Column(db.String(255))
    json = db.Column(JSONType)
    users = db.Column(JSONType)
    admin_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    uuid = db.Column(db.String(255))
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))  # noqa: E501
    clusters = db.relationship("Cluster")
