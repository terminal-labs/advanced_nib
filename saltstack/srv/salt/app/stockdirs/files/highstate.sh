export DEESCALATED_SALT_CONFIG_DIR=/home/vagrant/lxc-cloud/saltstack/configs
export DEESCALATED_SALT_ROOT_DIR=/home/vagrant/lxc-cloud/saltstack/states
export DEESCALATED_SALT_LOG_FILE=/home/vagrant/lxc-cloud/saltstack/logs/logs
sudo -E salt-call \
   --config-dir=$DEESCALATED_SALT_CONFIG_DIR \
   --log-file=$DEESCALATED_SALT_LOG_FILE \
   --file-root=$DEESCALATED_SALT_ROOT_DIR \
   --log-level=info \
   --local state.highstate
