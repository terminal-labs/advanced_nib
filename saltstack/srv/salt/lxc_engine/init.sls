install_lxd_service_daemon:
  cmd.run:
    - name: apt install -y lxd

start_lxc_service_daemon:
  cmd.run:
    - name: "service lxd start"

/tmp/lxccloud:
  file.directory:
    - user: vagrant
    - name: /tmp/lxccloud
    - group: vagrant
    - mode: 777

lxd_conf:
  file.managed:
    - name: /tmp/lxccloud/lxd_preseed.yaml
    - source: salt://lxc_engine/lxd_preseed.yaml

run_lxc_init:
  cmd.run:
    - name: cat /tmp/lxccloud/lxd_preseed.yaml | lxd init --preseed

clone_base_image:
  cmd.run:
    - name: 'lxc image copy ubuntu:18.04 local: --alias ubuntu:18.04'

/home/vagrant/.config/lxc:
  file.directory:
    - user: vagrant
    - name: /home/vagrant/.config/lxc
    - group: vagrant
    - mode: 777

set_socket_perms:
  cmd.run:
    - name: 'chown vagrant /var/lib/lxd/unix.socket'