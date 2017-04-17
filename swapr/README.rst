SWAPR Playbooks
===============

The top-level ``*.yml`` files in this directory are playbooks for various
pieces of SWAPR infrastructure. These determine what gets done on
the machines being provisioned/modified.

To provision your locally running VM as a standard development environment,
fire up your VM via ``vagrant up`` and run:

    vagrant provision

**Note: These playbooks are in varying states of readiness, and many are
very experimental at this point. If something doesn't work locally,
the playbook probably isn't finished yet.**


ansible-galaxy install -r roles.txt