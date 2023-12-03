create_persistent_working_dirs:
  cmd.run:
    - name: >
        mkdir -p /persistentworkingdirs;

create_uploads_dir:
  cmd.run:
    - name: >
        mkdir -p /persistentworkingdirs/uploads;

create_files_dir:
  cmd.run:
    - name: >
        mkdir -p /persistentworkingdirs/files;

deploy_file_enable_ssh:
  file.managed:
    - name: /persistentworkingdirs/files/enable_ssh.sh
    - source: salt://app/stockdirs/files/enable_ssh.sh

deploy_file_highstate:
  file.managed:
    - name: /persistentworkingdirs/files/highstate.sh
    - source: salt://app/stockdirs/files/highstate.sh

deploy_file_demo_cluster:
  file.recurse:
    - name: /persistentworkingdirs/demo-cluster
    - source: salt://app/stockdirs/demo-cluster

set_persistent_working_dirs_perms:
  cmd.run:
    - name: >
        chmod -R 777 /persistentworkingdirs;
