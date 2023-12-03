apt_update_for_postgresql:
  cmd.run:
    - name: apt update

install_postgresql:
  cmd.run:
    - name: apt install -y postgresql postgresql-contrib

start_postgresql:
  cmd.run:
    - name: service postgresql start

set_postgresql_password:
  cmd.run:
    - name: psql -c "ALTER USER postgres PASSWORD 'PASSWORD';"
    - runas: postgres
