from humbledb import Document

from lxccloud.settings import MONGO_DB


class Clusters_mgdb(Document):
    config_database = MONGO_DB
    config_collection = "clusters"
    description = "d"
    value = "v"
