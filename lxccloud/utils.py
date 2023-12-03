import os
import json
import base64
import random
import string

from pathlib import Path
from shutil import copyfile, move, rmtree
from subprocess import Popen, PIPE


def b64encode(data):
    assert isinstance(data, bytes) is True
    return base64.b64encode(data)


def random_tag():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def dir_exists(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    return os.path.isdir(path)


def dir_create(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)


def dir_delete(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    rmtree(path)


def file_delete(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    os.remove(path)


def file_read(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    file_obj = open(path, "rb")
    data = file_obj.read()
    file_obj.close()
    return data


def file_write(path, data):
    assert isinstance(path, str) is True
    assert isinstance(data, str) is True
    path = os.path.abspath(path)
    file_obj = open(path, "wb")
    file_obj.write(data.encode("utf-8"))
    file_obj.close()


def file_read_json(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    file_data = file_read(path)
    dic = json.loads(file_data)
    return dic


def file_copy(src, dst):
    assert isinstance(src, str) is True
    assert isinstance(dst, str) is True
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    copyfile(src, dst)


def file_rename(src, dst):
    assert isinstance(src, str) is True
    assert isinstance(dst, str) is True
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    os.rename(src, dst)


def file_move(src, dst):
    assert isinstance(src, str) is True
    assert isinstance(dst, str) is True
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    move(src, dst)


def get_user_home():
    return str(Path.home())


def get_env_variable(name):
    assert isinstance(name, str) is True
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


def print_kv_pairs(dic):
    assert isinstance(dic, dict) is True
    for key in dic.keys():
        print(f"{key} =", dic[key])


def list_files(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    return [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]  # noqa: E501


def list_file_paths(path):
    assert isinstance(path, str) is True
    path = os.path.abspath(path)
    file_paths = []
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            file_paths.append(os.path.abspath(os.path.join(root, filename)))
    return file_paths


def __realtime_call(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        line = line.decode("utf-8")
        if not line:
            break
        yield line


def call_ssh_generator(user, host, command):
    for line in __realtime_call(f"ssh {user}@{host} '{command}'"):
        if not line:
            break
        yield line


def call_ssh(user, host, command):
    result = []
    for line in __realtime_call(f"ssh {user}@{host} '{command}'"):
        result.append(line + "\n")
    result = "".join([str(x) for x in result])
    return result


def call_local_shell(command):
    result = []
    for line in __realtime_call(f"{command}"):
        result.append(line + "\n")
    result = "".join([str(x) for x in result])
    return result
