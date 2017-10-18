# SWAPR provisioning repository

## Getting started
To provision a local copy of the SWAPR development environment, first ensure that you have the following dependencies:

- [Docker]

Next, run the following commands to clone the repository and build the environment.

```bash
git clone git@github.com:GatechVIP/gatech-swapr-provisioning.git
git submodule init
git submodule update
docker-compose up --build
```

Then, on your host machine, port 8080 should point to the nginx service which should be serving the most recent build (in the `dist` directory) of the client code.

From here, just make sure to use the copies of the client and server code that are found as submodules of this repo. Whenever there is an update to one of the submodules,
just make sure to run `git submodule update` in the provisioning repo.

[Docker]: <https://store.docker.com/search?type=edition&offering=community>