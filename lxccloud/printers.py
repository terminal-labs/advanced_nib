from contracts import contract
from texttable import Texttable

from lxccloud.settings import VERSION as versionnumber, DB_URL, TEXTTABLE_STYLE

from lxccloud.pdf_subsystem import render_pdf_html, generate_pdf
from lxccloud.lxc_subsystem import list_container_ips, list_container_names

from lxccloud.core import (
    test_pgdb_conn,
    test_mgdb_conn,
    generate_cluster_spec,
    store_imported_file_from_path,
    compile_list_of_uploaded_files,
    __create_cluster,
    __list_clusters,
    __delete_cluster,
)


@contract(returns=None)
def print_testfunc():
    print(render_pdf_html())

    # print(random_tag())
    # t = Texttable()
    # t.set_chars(["-", "|", "+", "-"])
    # t.add_rows([["Name", "Age"], ["Alice", 24], ["Bob", 19]])
    # print(t.draw())
    # print(call_local_shell("df -h"))
    # for line in call_ssh_generator("vagrant",
    #                                "127.0.0.1",
    #                                "apt update"):
    #    print(line)
    # print(hydrate_cluster_registry())


@contract(returns=None)
def print_version():
    print(versionnumber)


@contract(returns=None)
def print_kv_pairs(dic):
    assert isinstance(dic, dict) is True
    for key in dic.keys():
        print(f"{key} =", dic[key])


@contract(returns=None)
def print_listcontainernames():
    for container_name in list_container_names():
        print(container_name)


@contract(returns=None)
def print_listcontainerips():
    for container_data in list_container_ips():
        print(container_data[0], container_data[1])


@contract(returns=None)
def print_showdbconnstring():
    print(DB_URL)


@contract(returns=None)
def print_test_pgdb_conn():
    print(test_pgdb_conn())


@contract(returns=None)
def print_test_mgdb_conn():
    print(test_mgdb_conn())


@contract(returns=None)
def print_generate_cluster_spec(clustername):
    print(generate_cluster_spec(clustername))


@contract(returns=None)
def print_generate_pdf(html):
    print(generate_pdf(html))


@contract(returns=None)
def print_upload_cluster_specification_file(specfilepath):
    print(store_imported_file_from_path(specfilepath))


@contract(returns=None)
def print_list_of_uploaded_files():
    list_of_uploaded_files = compile_list_of_uploaded_files()
    t = Texttable()
    t.set_chars(TEXTTABLE_STYLE)
    t.add_row(["NAME", "SIZE", "HASH"])
    for uploadfile in list_of_uploaded_files:
        t.add_row([uploadfile, "Not Implemented", "Not Implemented"])
    print(t.draw())


@contract(returns=None)
def print_create_cluster():
    __create_cluster()


@contract(returns=None)
def print_list_clusters():
    clusters = __list_clusters()
    t = Texttable()
    t.set_chars(TEXTTABLE_STYLE)
    t.add_row(["ID"])
    for cluster in clusters:
        t.add_row([cluster["_id"]])
    print(t.draw())


@contract(returns=None)
def print_delete_cluster(id):
    __delete_cluster(id)
