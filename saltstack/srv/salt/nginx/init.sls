nginx_install:
  cmd.run:
    - name: apt install -y nginx-full

/etc/nginx/sites-enabled/default:
  file.absent

nginx_conf:
  file.managed:
    - name: /etc/nginx/sites-enabled/nginx.conf
    - template: jinja
    - source: salt://nginx/nginx.conf

nginx_restart:
  cmd.run:
    - name: service nginx restart
