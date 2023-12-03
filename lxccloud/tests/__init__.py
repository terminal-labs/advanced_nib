import time
import subprocess

from pylxd import Client as lxdclient

client = lxdclient()


def list_container_names():
    containers = client.containers.all()
    names = []
    for container in containers:
        names.append(container.name)
    return names


def list_container_ips():
    names = list_container_names()
    results = []
    for name in names:
        container = client.containers.get(name)
        ip = container.state().network["eth0"]["addresses"][0]["address"]
        results.append((name, ip))
    return results


def __prepare_container(name):
    cmd = f"lxc file push lxc_subsystem/enable_ssh.sh {name}/enable_ssh.sh"  # noqa: E501
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()  # noqa: E501

    cmd = f"lxc exec {name} -- bash /enable_ssh.sh"
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()


def __create_container(name, alias):
    config = {"name": name, "source": {"type": "image", "alias": alias}}
    container = client.containers.create(config, wait=True)
    container.start()

    while container.state().network is None:
        time.sleep(1)

    while container.state().network["eth0"]["addresses"][0]["family"] != "inet":  # noqa: E501
        time.sleep(1)

    __prepare_container(name)
    return container


def create_container(name, alias):
    return __create_container(name, alias)
