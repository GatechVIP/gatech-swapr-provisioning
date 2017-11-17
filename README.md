# SWAPR provisioning repository

## Repository explanation
This repository contains the Docker Compose and Stack files for SWAPR that are needed to provision a development environment or deploy to production.

### Notable files
- `docker-compose.yaml`: The base service configuration for our whole stack. Defines three services: db, backend, www. Service configuration in this file, when possible, should only be for configuration values that do not differ from environment to environment.
- `docker-compose.override.yaml`: Development overrides for the base Docker Compose file.
- `docker-compose.production.yaml`: To be created. Production overrides for the base Docker Compose file.
- `docker-compose.test.yaml`: To be created. Docker environment for running our test suite with a fresh start every time.

## Initial setup
To make sure that we use SSL for our development environment, we use the hostname `swapr-dev.vip.gatech.edu` to access the development enviornment. This hostname doesn't actually resolve to anything on Georgia Tech's DNS, so we'll need to add is to your host system's local DNS resolver manually.

See Rackspace's article on how to [modify your hosts file]. Add the following entry to your hosts file:

```
127.0.0.1 swapr-dev.vip.gatech.edu
```

You should now be able to run `ping swapr-dev.vip.gatech.edu` to see it resolving to `127.0.0.1`.

You'll then need to download the self-signed development SSL certificate to add it to your operating system's trust store: [Download certificate]

Then, to add it to your operating system's trust store so you don't get SSL warnings in your browser. If you're unfamiliar with the process, follow the guide below for your operating system. Only the macOS guide has been tested, so create an issue in the provisioning repository if that's the case.

- [Windows]
- [macOS]
- Linux: could be managed by your browser or your distro, look up how to trust self-signed certificates for your particular distro and browser.


[Modify your hosts file]: <https://support.rackspace.com/how-to/modify-your-hosts-file/>
[Download certificate]: <>
[Windows]: <https://community.spiceworks.com/how_to/1839-installing-self-signed-ca-certificate-in-windows>
[macOS]: <https://tosbourn.com/getting-os-x-to-trust-self-signed-ssl-certificates/>

## Getting started
To provision a local copy of the SWAPR development environment, first ensure that you have the following dependencies:

- [Docker]

Next, run the following commands to clone the repository and build the environment.

```bash
git clone --recursive git@github.com:GatechVIP/gatech-swapr-provisioning.git
docker-compose up --build
```

The `--recursive` flag on our clone command automatically pulls the two git submodules for the backend and frontend from their separate repositories on GitHub. If you're unfamiliar with git submodules, here are some implications to keep in mind:

- The backend and frontend repositories are totally separate and have their own history.
- Git submodules in the provisioning repo (this one) are pinned to a particular commit hash for each submodule. This means that after committing and pushing changes in a submodule, you need to `git add <name of submodule directory>` and commit that change to the provisioning repo for the provisioning repo to have the correct references to the latest version of that part of the codebase.
- All git submodules can be automatically updated to their newest versions by running `git submodule update --remote`.

When `docker-compose up --build` executes, it will build the server container and update it to the latest version, as well as run the PostgreSQL container and the nginx container. All of the output will stay in the same console.

Alternatively, you can run the environment as a daemon in the background, if you don't need to view the logs, using `docker-compose up -d --build`. To stop the environment, run `docker-compose down`.

After starting the evnironment on your host machine, port 8443 on your host should point to the nginx service which should be serving the most recent build (in the `dist` directory) of the client code.

Access the development server via your browser to make sure it is working. Some details about the development server:

- Accessible from your host machine at https://swapr-dev.vip.gatech.edu:8443/
- API root is https://swapr-dev.vip.gatech.edu:8443/api/
- Login route is proxied to the backend at https://swapr-dev.vip.gatech.edu:8443/login/
- We need to use a .gatech.edu local dev domain or we can't test CAS login

From here, just make sure to use the copies of the client and server code that are found as submodules of this repo. Whenever there is an update to one of the submodules,
just make sure to run `git submodule update` in the provisioning repo.

[Docker]: <https://store.docker.com/search?type=edition&offering=community>

## Provisioning

To run your SWAPR instance with docker, run `docker-compose up --build` to start all three services (db, backend, www) in the same console. The services will stay alive until one encounters a fatal error, or a `Ctrl-C` is issued in the terminal.

If you need to run commands on the backend container, you can run `docker-compose exec backend bash` in a separate terminal to start a shell. This is useful for running `sequelize` commands for database migrations.

## Next steps
Here are a list of tasks that still need to be accomplished for this Docker environment.

- General
    - Make sure that that `config.json` located in `config/backend-config.json` is correct and can be used for all build configurations
    - Add appropriate environmental variables based on build configurations
    - Set secret key in backend config.json
    - Convert everything into a mono-repo
- Production
    - Create `production.yml` for production settings
        - Make sure to use client `dist`
        - Use port `80` and `443` for nginx
        - Docker secrets
    - Provision SSL certificate for `swapr.vip.gatech.edu` and add to the repo
- Development
    - Test and make sure that links between development code on the host work and can be used without trouble
        - Use client development build directory -- try to support a watch command for building on dev -- maybe a separate container?
    - Set up proxy URL, something like `swapr.local` that proxies to `www:8080`
- Testing
    - Create a docker compose environment for running the test suite in the production environment

Notes on production compose/stack file:

- We need to set the UID and GID of any secrets for the backend service to `1000`
- Secrets for the db and backend services should be configured, with `{env_var}_FILE` environment variables set to the path of the secret

Pending docs improvements:

- Add more of a Docker Compose tutorial
- Explain how the stack works and communicates
- Move all of this to the GitHub wiki in separate, digestible sections