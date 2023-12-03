remove_mongo:
  cmd.run:
    - name: sudo service mongod stop; sudo apt-get purge mongodb-org*; sudo apt-get -f install

install_mongo:
  pkg.installed:
    - pkgs:
      - mongodb
