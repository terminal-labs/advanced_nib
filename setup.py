import sys
from setuptools import setup, find_packages

from lxccloud.settings import VERSION, MINIMUM_PYTHON_VERSION

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="lxc-cloud",
    version=VERSION,
    description="lxc cloud",
    author="Terminal Labs",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "utilities-package@git+https://gitlab.com/terminallabs/utilitiespackage/utilities-package.git",
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-mock",
        "pytest-click",
        "pytest-pylint",
        "pytest-httpserver",
        "black",
        "flake8",
        "radon",
        "sqlalchemy",
        "flask",
        "flask-login",
        "flask-security",
        "flask-sqlalchemy",
        "flask-caching",
        "sqlalchemy-utils",
        "psycopg2-binary",
        "pylibmc",
        "pymongo",
        "humbledb",
        "bcrypt",
        "requests",
        "cherrypy",
        "django-htmlmin",
        "xvfbwrapper",
        "pdfkit",
        "pylxd",
        "texttable",
        "cli-passthrough",
        "pycontracts",
    ],
    entry_points="""
        [console_scripts]
        lxccloud=lxccloud.__main__:main
    """,
)
