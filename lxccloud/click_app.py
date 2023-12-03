import pytest
import click

from lxccloud.settings import server_port, socket_host, CONFIG_DIC, BASEDIR, PAYLOADPATH

from lxccloud.cherrypy_app import cherrypy as cherrypy_app
from lxccloud.flask_app import app as flask_app
from lxccloud.core import callsalt, __create_container, delete_uploaded_file, delete_all_uploaded_files
from lxccloud.printers import (
    print_version,
    print_testfunc,
    print_kv_pairs,
    print_listcontainernames,
    print_listcontainerips,
    print_showdbconnstring,
    print_test_pgdb_conn,
    print_test_mgdb_conn,
    print_generate_cluster_spec,
    print_generate_pdf,
    print_upload_cluster_specification_file,
    print_list_of_uploaded_files,
    print_create_cluster,
    print_list_clusters,
    print_delete_cluster,
)


@click.group()
def cli():
    return None


@click.group(name="clusters")
def clusters():
    return None


@click.group(name="pdf-operations")
def pdf():
    return None


@click.group(name="lxc-operations")
def lxc():
    return None


@click.group(name="salt-operations")
def salt():
    return None


@click.group()
def servers():
    return None


@click.group()
def testing():
    return None


@click.group()
def helpers():
    return None


@clusters.command()
def createcluster():
    print_create_cluster()


@clusters.command()
@click.argument("id")
def deletecluster(id):
    print_delete_cluster(id)


@clusters.command()
def listclusters():
    print(PAYLOADPATH)
    # print_list_clusters()


@lxc.command()
def listcontainernames():
    print_listcontainernames()


@lxc.command()
def listcontainerips():
    print_listcontainerips()


@lxc.command()
@click.argument("containername")
def createcontainer(containername):
    __create_container(containername, "ubuntu:18.04")


@testing.command()
def testpgdbconn():
    print_test_pgdb_conn()


@testing.command()
def testmgdbconn():
    print_test_mgdb_conn()


@testing.command()
def selftest():
    pytest.main(["-x", "-v", BASEDIR])


@testing.command()
def selfcoverage():
    pytest.main(["--cov", BASEDIR, "--cov-report", "term-missing"])


@salt.command(name="callsalt")
def callsalt_command():
    callsalt()


@pdf.command()
@click.option("--dryrun", default=1, show_default=True)
def createpdf(dryrun):
    if dryrun == 1:
        html = "test data"
        print_generate_pdf(html)
    else:
        return None


@cli.command()
def version():
    print_version()


@testing.command()
def showdbconnstring():
    print_showdbconnstring()


@testing.command()
def showvars():
    print_kv_pairs(CONFIG_DIC)


@testing.command()
def testfunc():
    print_testfunc()


@servers.command()
def runcherrypyserver():
    cherrypy_app.engine.start()


@servers.command()
def runflaskserver():
    flask_app.run(host=socket_host, port=server_port)


@helpers.command()
@click.argument("clustername")
def export_cluster_spec(clustername):
    print_generate_cluster_spec(clustername)


@helpers.command()
@click.argument("specfilepath")
def import_cluster_spec(specfilepath):
    print_upload_cluster_specification_file(specfilepath)


@helpers.command(name="list-uploaded-files")
def list_uploaded_file_command():
    print_list_of_uploaded_files()


@helpers.command(name="delete-uploaded-file")
@click.argument("filename")
def delete_uploaded_file_command(filename):
    delete_uploaded_file(filename)


@helpers.command(name="delete-all-uploaded-files")
def delete_all_uploaded_files_command():
    delete_all_uploaded_files()


cli.add_command(clusters)
cli.add_command(servers)
cli.add_command(testing)
cli.add_command(salt)
cli.add_command(lxc)
cli.add_command(pdf)
cli.add_command(helpers)
main = cli
