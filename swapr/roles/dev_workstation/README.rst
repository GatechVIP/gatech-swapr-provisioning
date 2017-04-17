dev_workstation role
====================

This roles, when used in conjunction with roles/node_host, leaves us
with a functional developer environment.

post_node_host runs after the node_host role. It finishes up by setting
up Samba/SSH keys.