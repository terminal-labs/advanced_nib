import os
import tempfile

from lxccloud.derived_settings import APPDIR, SITEPACKAGESPATH
from lxccloud.resolved_settings import get_env_variable, resolve_payload_path

reponame = "lxc-cloud"


def set_vars():
    VERSION = "0.0.3"
    PRINT_VERBOSITY = "high"
    EXCLUDED_DIRS = [".DS_Store"]
    SETUP_NAME = reponame
    PROJECT_NAME = SETUP_NAME.replace("_", "").replace("-", "")
    EGG_NAME = SETUP_NAME.replace("_", "-")
    TEMPDIR = "/tmp"
    TEXTTABLE_STYLE = ["-", "|", "+", "-"]
    DIRS = [f"{TEMPDIR}/{SETUP_NAME}workingdirs"]
    MINIMUM_PYTHON_VERSION = (3, 6, 0)
    COVERAGERC_PATH = f"{APPDIR}/.coveragerc"
    PAYLOADPATH = SITEPACKAGESPATH   # noqa: F841
    server_port = 5000
    socket_host = "0.0.0.0"

    globals()["VERSION"] = VERSION
    globals()["PRINT_VERBOSITY"] = PRINT_VERBOSITY
    globals()["EXCLUDED_DIRS"] = EXCLUDED_DIRS
    globals()["SETUP_NAME"] = SETUP_NAME
    globals()["PROJECT_NAME"] = PROJECT_NAME
    globals()["EGG_NAME"] = EGG_NAME
    globals()["TEMPDIR"] = TEMPDIR
    globals()["TEXTTABLE_STYLE"] = TEXTTABLE_STYLE
    globals()["DIRS"] = DIRS
    globals()["MINIMUM_PYTHON_VERSION"] = MINIMUM_PYTHON_VERSION
    globals()["COVERAGERC_PATH"] = COVERAGERC_PATH
    globals()["SITEPACKAGESPATH"] = SITEPACKAGESPATH
    globals()["server_port"] = server_port
    globals()["socket_host"] = socket_host

    return {
        "VERSION": VERSION,
        "PRINT_VERBOSITY": PRINT_VERBOSITY,
        "EXCLUDED_DIRS": EXCLUDED_DIRS,
        "SETUP_NAME": SETUP_NAME,
        "PROJECT_NAME": PROJECT_NAME,
        "EGG_NAME": EGG_NAME,
        "TEMPDIR": TEMPDIR,
        "TEXTTABLE_STYLE": TEXTTABLE_STYLE,
        "DIRS": DIRS,
        "MINIMUM_PYTHON_VERSION": MINIMUM_PYTHON_VERSION,
        "COVERAGERC_PATH": COVERAGERC_PATH,
        "SITEPACKAGESPATH": SITEPACKAGESPATH,
        "server_port": server_port,
        "socket_host": socket_host,
    }


set_vars()

PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821

POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)
MONGO_DB = PROJECT_NAME  # noqa: F821
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
BASEDIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
CLUSTER_DIR = os.path.join(ROOT_DIR, "clusters")
STATIC_DIR = os.path.join(PAYLOADPATH, "static")
PERSISTENT_WORKING_DIRS = "stub"
CONFIG_DIC = {"POSTGRES_URL": POSTGRES_URL, "POSTGRES_USER": POSTGRES_USER, "POSTGRES_PW": POSTGRES_PW, "POSTGRES_DB": POSTGRES_DB}

tempfile.tempdir = TEMPDIR  # noqa: F821
