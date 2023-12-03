from flask import Blueprint
from flask import render_template, jsonify, make_response
from flask import send_from_directory
from flask_security.core import current_user
from htmlmin.minify import html_minify

from lxccloud.settings import TEMPLATE_DIR, PAYLOADPATH

from lxccloud.pdf_subsystem import render_pdf_html, generate_pdf
from lxccloud.core import hydrate_cluster_registry
from lxccloud.system_info import get_box_specs
from lxccloud.cache import cache

gui_blueprint = Blueprint("gui_blueprint", __name__, template_folder=TEMPLATE_DIR)  # noqa: E501

gui_root = "gui"
gui_version = "1.0"
gui_spec_version = "0.1"
gui_status = "good"
gui_test_dic = {"status": gui_status}
gui_info_dic = {"status": gui_status, "version": gui_version, "system": gui_root}


@gui_blueprint.route("/")
# @login_required
def index():
    return html_minify(render_template("index.html", title="Dashboard"))


@gui_blueprint.route("/create-cluster")
# @login_required
def create_cluster():
    clusters = []
    demo = hydrate_cluster_registry()
    clusters.append(demo)
    return render_template("create-cluster.html", title="Dashboard", clusters=clusters)  # noqa: E501


@gui_blueprint.route("/clusters")
# @login_required
def clusters():
    return render_template("clusters.html", title="Dashboard")


@gui_blueprint.route("/cluster/<cluster_name>")
# @login_required
def single_cluster(cluster_name):
    return render_template("single-cluster.html", cluster_name=cluster_name, title="Dashboard")


@gui_blueprint.route("/blog")
# @login_required
@cache.cached(timeout=50)
def blog():
    return render_template("blog.html", title="Dashboard")


@gui_blueprint.route("/signup")
# @login_required
def sign_up():
    return render_template("sign-up.html", title="Dashboard")


@gui_blueprint.route("/login")
# @login_required
def log_in(name=None):
    return render_template("log-in.html", name=name, title="Dashboard")


@gui_blueprint.route("/settings")
# @login_required
def settings():
    return render_template("settings.html", title="Dashboard")


@gui_blueprint.route("/billing")
# @login_required
def billing():
    return render_template("billing.html", title="Dashboard")


@gui_blueprint.route("/accounts")
# @login_required
def accounts():
    username = current_user.email
    return render_template("accounts.html", title="Dashboard", username=username)  # noqa: E501


@gui_blueprint.route("/test")
# @login_required
def system_test():
    return render_template("test.html", title="test")


@gui_blueprint.route("/boxinfo")
def gui_boxinfo():
    return get_box_specs()


@gui_blueprint.route("/files/pdf/34234")
# @login_required
def create_pdf():
    html = render_pdf_html()
    response = make_response(generate_pdf(html))
    response.headers["Content-type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=out.pdf"
    return response


@gui_blueprint.route("/static/<filename>")
@gui_blueprint.route("/static/<path:path>/<filename>")
def custom_static(filename, path=None):
    if not path:
        path = ""
    return send_from_directory(PAYLOADPATH + "/static/" + path, filename)


@gui_blueprint.route("/system/health")
def gui_health():
    return jsonify({"status": "healthy"})


@gui_blueprint.route("/system/test")
def gui_test():
    return jsonify(gui_test_dic)


@gui_blueprint.route("/system/info")
def gui_info():
    return jsonify(gui_info_dic)
