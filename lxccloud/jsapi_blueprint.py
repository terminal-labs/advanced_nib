from flask import Blueprint
from flask import jsonify

from lxccloud.settings import TEMPLATE_DIR

jsapi_blueprint = Blueprint("jsapi_blueprint", __name__, template_folder=TEMPLATE_DIR)  # noqa: E501

jsapi_root = "js-api"
jsapi_version = "1.0"
jsapi_spec_version = "0.1"
jsapi_status = "good"
jsapi_test_dic = {"status": jsapi_status}
jsapi_info_dic = {"status": jsapi_status, "version": jsapi_version, "system": jsapi_root}


# @jsapi_blueprint.route(f"/{jsapi_root}/v" + jsapi_version + "/post/echo", methods=["GET", "POST"])  # noqa: E501
# def jsapi_post():
#     return jsonify({"status": jsapi_status})
#
#
# @jsapi_blueprint.route(f"/{jsapi_root}/v" + jsapi_version + "/post/generalclusterinfo", methods=["POST"])
# def jsapi_general_cluster_info():
#     requested_name = request.json["name"]
#     dic = get_json_dict_from_dir(requested_name, "resources/public_cluster_specs")  # noqa: E501
#     return jsonify(dic)
#
#
# @jsapi_blueprint.route(f"/{jsapi_root}/v" + jsapi_version + "/post/anyactivebuilds", methods=["POST"])
# def jsapi_any_active_builds():
#     return jsonify("no")
#
#
# @jsapi_blueprint.route(f"/{jsapi_root}/v" + jsapi_version + "/post/createcluster", methods=["POST"])
# def internal_api():
#     c = Cluster()
#     current_user.clusters.append(c)
#     c = Cluster()
#     current_user.clusters.append(c)
#     db.session.commit()
#     request.json["name"]
#     return jsonify(status="good")


@jsapi_blueprint.route(f"/{jsapi_root}/v" + jsapi_version + "/post/rpc", methods=["POST"])
def jsapi_rpc():
    return jsonify("no")


@jsapi_blueprint.route(f"/{jsapi_root}/system/health")
def jsapi_health():
    return jsonify({"status": "healthy"})


@jsapi_blueprint.route(f"/{jsapi_root}/system/test")
def jsapi_test():
    return jsonify(jsapi_test_dic)


@jsapi_blueprint.route(f"/{jsapi_root}/system/info")
def jsapi_info():
    return jsonify(jsapi_info_dic)
