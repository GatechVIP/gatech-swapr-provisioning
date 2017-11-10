# SWAPR provisioning repository

## Repository explanation
This repository contains the Docker Compose and Stack files for SWAPR that are needed to provision a development environment or deploy to production.

### Notable files
- `docker-compose.yaml`: The base service configuration for our whole stack. Defines three services: db, backend, www. Service configuration in this file, when possible, should only be for configuration values that do not differ from environment to environment.
- `docker-compose.override.yaml`: Development overrides for the base Docker Compose file.
- `docker-compose.production.yaml`: To be created. Production overrides for the base Docker Compose file.
- `docker-compose.test.yaml`: To be created. Docker environment for running our test suite with a fresh start every time.

## Getting started
To provision a local copy of the SWAPR development environment, first ensure that you have the following dependencies:

- [Docker]

Next, run the following commands to clone the repository and build the environment.

```bash
git clone --recursive git@github.com:GatechVIP/gatech-swapr-provisioning.git
docker-compose up --build
```

In addition, when updating submodules (client and server), run `git submodule update --remote`.

Then, on your host machine, port 8080 should point to the nginx service which should be serving the most recent build (in the `dist` directory) of the client code.

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
        - Use client development build directory
    - Provision local self-signed SSL certificate for use during development
    - Set up proxy URL, something like `swapr.local` that proxies to `www:8080`
- Testing
    - Create a docker compose environment for running the test suite in the production environment

Notes on production compose/stack file:
- We need to set the UID and GID of any secrets for the backend service to `1000`
- Secrets for the db and backend services should be configured, with `{env_var}_FILE` environment variables set to the path of the secret