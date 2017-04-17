Provisioning and Deploy Repo
============================

This repository contains everything needed to provision the
full SWAPR architecture. The tools of the trade are:

* `Ansible`_ - Provisioning of dev, staging, and prod infrastructure.
* `Vagrant`_ - Used to run local VM deploys of the infrastructure.
* `VirtualBox`_ - Virtualization software used by Vagrant.

Provisioning a development environment
--------------------------------------

There will be a guide here for this... soon.

Provisioning infrastructure
---------------------------

If you are wanting to provision production infrastructure::

    pip install -r requirements.txt

Then ``cd`` into ``swapr`` and launch the playbook of your choice
according to the ``README.rst`` there.

.. _Ansible: http://www.ansibleworks.com/
.. _Vagrant: http://www.vagrantup.com/
.. _VirtualBox: https://www.virtualbox.org/
