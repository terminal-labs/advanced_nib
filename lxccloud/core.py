import os
import datetime

from multiprocessing import Process

from pymongo import MongoClient
from humbledb import Mongo
from bson.objectid import ObjectId
from sqlalchemy import create_engine
from contracts import contract

from cli_passthrough import cli_passthrough
from lxccloud.lxc_subsystem import create_container
from lxccloud.models_mgdb import Clusters_mgdb

from lxccloud.utils import (
    list_file_paths,
    file_read,
    file_write,
    file_delete,
    b64encode,
    dir_exists,
    dir_create,
    file_read_json,
    random_tag,
    list_files,
)  # noqa: E501
from lxccloud.settings import DB_URL, CLUSTER_DIR


def test_pgdb_conn():
    raw_engine = create_engine(DB_URL)
    raw_conn = raw_engine.connect()
    raw_conn.execute(
        """CREATE TABLE IF NOT EXISTS films (title text,
        director text,
        year text)"""
    )
    result = raw_conn.execute(
        """select column_name,
        data_type from information_schema.columns where table_name = 'films'"""
    )
    rows = result.fetchall()
    raw_conn.close()

    s = ""
    for row in rows:
        s = s + str(row) + "\n"
    return s


def test_mgdb_conn():
    client = MongoClient("localhost", 27017)
    db = client["test-database"]
    collection = db["test-collection"]
    articles = collection.articles
    # articles.remove({"author": "Mike"})
    if articles.find_one({"author": "Mike"}) is None:
        post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
        articles.insert_one(post)

    for article in articles.find():
        print(article)
    return "result.inserted_id"


def invoke_salt(args):
    cmd = """bash salt_subsystem/highstate.sh"""
    cli_passthrough(cmd)


def generate_cluster_spec(clustername):
    if dir_exists(os.path.join(CLUSTER_DIR, clustername)):
        cluster = clustername
        file_paths = list_file_paths(os.path.join(CLUSTER_DIR, clustername))
        for file_path in file_paths:
            print(b64encode(file_read(file_path)))
            file_path = file_path.replace(f"{CLUSTER_DIR}/{cluster}/", "")
            print(file_path)
    else:
        raise IOError(f"cluster named '{clustername}' does not exist")


def hydrate_cluster_registry():
    clustername = "demo"
    json_file_path = os.path.join(CLUSTER_DIR, clustername, "spec.json")
    return file_read_json(json_file_path)  # os.listdir(CLUSTER_DIR)


def callsalt():
    salt_process = Process(target=invoke_salt, args=(None,))
    salt_process.start()


def __create_container(name, alias):
    create_container(name, alias)


def store_imported_file_from_path(filepath):
    filedata = file_read(filepath)
    filedata = filedata.decode("utf-8")
    return store_imported_file_from_string(filedata)


def store_imported_file_from_string(filedata):
    uploads_dir = "/tmp/lxccloud/uploads"
    dir_create(os.path.abspath(uploads_dir))
    tag = random_tag()
    filepath = os.path.abspath(os.path.join(uploads_dir, tag))
    file_write(filepath, filedata)
    return {"tag": tag, "length": len(filedata)}


def delete_uploaded_file(filename):
    path = "/tmp/lxccloud/uploads"
    filepath = os.path.abspath(os.path.join(path, filename))
    file_delete(filepath)


def delete_all_uploaded_files():
    filelist = compile_list_of_uploaded_files()
    for f in filelist:
        delete_uploaded_file(f)


def compile_list_of_uploaded_files():
    path = "/tmp/lxccloud/uploads"
    dir_create(path)
    return list_files(path)


def __create_cluster():
    doc = Clusters_mgdb()
    doc.description = "The humblest document"
    doc.value = 3.14
    with Mongo:
        Clusters_mgdb.save(doc)
    print("create cluster -- good")


@contract(returns=tuple)
def __list_clusters():
    with Mongo:
        dics = []
        docs = Clusters_mgdb.find()
        for doc in docs:
            pr = {}
            for e in ["d", "v", "_id"]:
                pr[e] = str(doc[e])
            dics.append(pr)
        return tuple(dics)


@contract(id=str)
def __delete_cluster(id):
    with Mongo:
        Clusters_mgdb.remove({Clusters_mgdb._id: ObjectId(id)})
