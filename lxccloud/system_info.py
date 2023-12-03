import subprocess


def get_box_specs():
    info = subprocess.Popen("lsb_release -a", shell=True, stdout=subprocess.PIPE).stdout.read()
    return info
