import importlib

from ruamel.yaml import YAML


def conf(filepath):
    stream = open(filepath, "r")
    yaml = YAML(typ="safe")
    dict = yaml.load(stream)

    collectionfiles = {}
    for collection in dict["metadata"]["collections"]:
        module = importlib.import_module(collection + ".cli")
        payload_path = module._get_payload_path()
        for file in module._list_payload_files():
            collectionfiles[file] = payload_path
    return collectionfiles
