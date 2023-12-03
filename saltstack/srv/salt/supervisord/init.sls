install_supervisord:
  cmd.run:
    - name: apt install -y supervisor

supervisord_config_file:
  file.managed:
    - name: /etc/supervisor/conf.d/lxccloud.conf
    - source: salt://supervisord/lxccloud.conf.template

start_supervisord_service_daemon:
  cmd.run:
    - name: "service supervisor start"

start_supervisord_service_watcher:
  cmd.run:
    - name: "supervisorctl reread; supervisorctl update"
