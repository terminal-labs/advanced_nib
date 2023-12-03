delete_saltstack_saltcloud_null_provider_dir:
  cmd.run:
    - name: rm -rf /tmp/lxccloud/saltstack-saltcloud-null-provider

https://github.com/terminal-labs/saltstack-saltcloud-null-provider.git:
  git.latest:
    - user: vagrant
    - target: /tmp/lxccloud/saltstack-saltcloud-null-provider
    - branch: master

delete_saltstack_dir:
  cmd.run:
    - name: rm -rf /tmp/lxccloud/saltstack

https://github.com/saltstack/salt.git:
  git.latest:
    - user: vagrant
    - target: /tmp/lxccloud/saltstack
    - branch: v2018.3.3

delete_saltstack_git_dir:
  cmd.run:
    - name: rm -rf /tmp/lxccloud/saltstack/.git

delete_saltstack_github_dir:
  cmd.run:
    - name: rm -rf /tmp/lxccloud/saltstack/.github

zip_saltstack_dir:
  cmd.run:
    - cwd: /tmp/lxccloud
    - name: zip -q -r saltstack.zip saltstack
