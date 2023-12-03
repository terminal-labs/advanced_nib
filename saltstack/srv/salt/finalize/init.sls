/home/vagrant/lxc-cloud:
  file.directory:
    - user: vagrant
    - group: vagrant
    - mode: 777
    - recurse:
      - user
      - group
      - mode
    - require:
      - sls: apt
