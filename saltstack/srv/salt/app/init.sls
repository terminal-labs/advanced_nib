install_app:
  cmd.run:
    - name: >
        export PATH="/home/vagrant/dpe/lxccloud/miniconda3/bin:$PATH";
        source /home/vagrant/dpe/lxccloud/miniconda3/etc/profile.d/conda.sh;
        source auth/env/env.sh;
        conda activate lxccloud;
        pip install -e .;
    - cwd: /vagrant
    - runas: vagrant
