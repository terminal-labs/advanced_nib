apt_update_for_apt_requirements:
  cmd.run:
    - name: apt update

install_apt_requirements:
  cmd.run:
    - name: apt install -y lsb-core
