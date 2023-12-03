import cherrypy

from lxccloud.flask_app import app

from lxccloud.settings import server_port, socket_host

cherrypy.tree.graft(app, "/")
cherrypy.config.update({"server.socket_host": socket_host, "server.socket_port": server_port, "engine.autoreload.on": False})
