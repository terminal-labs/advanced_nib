import json

from flask import Blueprint, request, jsonify

from lxccloud.settings import TEMPLATE_DIR

from lxccloud.core import store_imported_file_from_string
from lxccloud.settings import ALLOWED_EXTENSIONS

fileioapi_blueprint = Blueprint("fileio_blueprint", __name__, template_folder=TEMPLATE_DIR)  # noqa: E501

fileioapi_root = "fileio-api"
fileioapi_version = "1.0"
fileioapi_spec_version = "0.1"
fileioapi_status = "good"
fileioapi_test_dic = {"status": fileioapi_status}
fileioapi_info_dic = {"status": fileioapi_status, "version": fileioapi_version, "system": fileioapi_root}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS  # noqa: E501


@fileioapi_blueprint.route("/files/upload", methods=["POST"])
def fileioapi_upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filedata = file.read()
            filedata = filedata.decode("utf-8")
            response_dic = store_imported_file_from_string(filedata)
            return json.dumps(response_dic)
    return "good"


@fileioapi_blueprint.route(f"/{fileioapi_root}/v" + fileioapi_version + "/post/rpc", methods=["POST"])
def fileioapi_rpc():
    return jsonify("no")


@fileioapi_blueprint.route(f"/{fileioapi_root}/system/health")
def fileioapi_health():
    return jsonify({"status": "healthy"})


@fileioapi_blueprint.route(f"/{fileioapi_root}/system/test")
def fileioapi_test():
    return jsonify(fileioapi_test_dic)


@fileioapi_blueprint.route(f"/{fileioapi_root}/system/info")
def fileioapi_info():
    return jsonify(fileioapi_info_dic)
