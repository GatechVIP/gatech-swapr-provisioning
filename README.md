# SWAPR provisioning
<a name="current-maintainer"></a>
**Current Maintainer:** Brad Reardon <<bradreardon@gatech.edu>>

The SWAPR provisioning repository is a series of Ansible playbooks that can provision multiple types of environments in order to run SWAPR for the Data-Driven Education VIP team. These playbooks are explained as follows:

- **Development**
	- `developer.yml` provisions the developer VM. [TODO] Instructions for using the development VM are inprogress. Use this only with Vagrant. To update the Vagrant VM with the newest developer playbook, run `vagrant provision` in the `swapr` directory.

- **Production**

	- `production.yml` for provisioning the production environment either from scratch or for updating system- or app-wide dependencies like `npm`. Use this playbook when either setting up a new server or when updating one to newer versions of the playbooks.
	
	- `deploy_to_prod.yml` [TODO] for deploying code updates **that don't require system-wide dependencies**. This will take care of updating `npm` dependencies via `npm install` and reloading `pm2`, our node process manager. When this is done, it will also make sure to either build the production environment, or will expect that a copy of the production client has already been built.

## Usage

### Repository usage notice
<a name="Repository-usage-notice"></a>

In order to use the majority of playbooks in this repository, you'll first have to have an SSH key generated for use in connecting to both development VMs and hosts in other environments like production.

For your convenience, we have a Google form that walks you through the onboarding process and in providing any information we may need to get you set up with provisioning. Please complete that form first and wait for a confirmation before attempting any of the below

### Components of the environment

In order to run Ansible playbooks, or to provision a development environment, you'll need to have a number of prerequisites installed:

- **Ansible:** A devops automation infrastructure, somewhat like configuration management. It uses YAML-defined "roles" to provide configuration for servers that meet different conditions.

	- **NOTE ON ANSIBLE:** Anytime a package is required on a server, we NEVER install that package on the server directly. Rather, we add it to the Ansible playbooks that define the functionality of that server, so that we have that package installed when provisioning future servers or reprovisioning ones that are out of date. That's what this repository is for, after all!

- **VirtualBox (dev only):** The virtual machine host that we use for development VMs. Should work on all platforms, but see the platform notice below if you experience any issues.

- **Vagrant (dev only):** Used to provision local VMs in tandem with Ansible. Interfaces with a VirtualBox virtual machine which is provisioned with Ansible. Does some of the underlying magic of installing a headless server VM like managing the configuration in VirtualBox so that you never have to use VirtualBox directly.

### Platform notice

These playbooks have only been tested extensively on a Mac host running macOS 10.11.6.

If you run into issues using these playbooks or provisioning the development environment on any other platform or version of any operating system, please notify the [repository maintainer] listed at the top of this document.

### Cloning the repository

First, make sure you have a recent version of [git] installed on your host machine

Find a cozy place on your host machine to clone this repository, probably near your other SWAPR code, and run the following clone command in a terminal:

	git clone https://github.com/GatechVIP/gatech-swapr-provisioning.git
	
Or, if you'd rather use Git over SSH (using public key authentication), use this clone command:

	git clone git@github.com:GatechVIP/gatech-swapr-provisioning.git

All of the provisioning playbooks and anything of particular resides in the `swapr` subdirectory.

[git]: <https://git-scm.com/>

### Running a playbook

The convention for running any non-development playbooks on hosts is with the following command:

	ansible-playbook -i hosts <playbook_name>.yml

#### A primer on hosts
The playbook itself specifies a tag in the hosts file to execute the playbook on. For example, `production.yml` specifies `hosts: production` which correspond to the `[production]` hosts in the `hosts` file. So, for example, if we ever provision multiple instances of the production app, we'd have a load balancer tag in the `hosts` file, and the new production server would be entered under `[production]`.

## Provisioning a Development Environment

### Before provisioning

Please read the [Repository usage notice] in the Usage section above.

[Repository usage notice]: <#Repository-usage-notice>

### Installing Prerequisites

1. Follow the steps for setting up Ansible on your platform with the current Ansible docs for [Installing the Control Machine].

2. Now, want to set up VirtualBox for your host. You should be able to find the binaries for your platform at the [VirtualBox downloads page].

3. Next, install Vagrant on your host machine. You can find the binaries for your platform at the [Vagrant downloads page].

[Installing the Control Machine]: <http://docs.ansible.com/ansible/intro_installation.html#installing-the-control-machine>

[VirtualBox downloads page]: <https://www.virtualbox.org/wiki/Downloads>

[Vagrant downloads page]: <https://www.vagrantup.com/downloads.html>

### Setting up the development virutal machine

1. Now that you've installed the prerequisites for your host machine, you're ready to spin up a development environment! Start off by opening a terminal and navigating your working directory to the `swapr` subdirectory of this repository's local clone.



## Contributing

Contributing to the provisioning repository of SWAPR helps our overall ability to deliver a stable application, as well as iterate on our in infrastructure to make sure that reponse times, database query times, and other development operations go smoothly and quickly.

If you're interested in helping maintain this repository, please contact the [repository maintainer] above, and they should be able to give you a walk through of the infrastructure and how to use Ansible to the fullest.

[repository maintainer]: <#current-maintainer>