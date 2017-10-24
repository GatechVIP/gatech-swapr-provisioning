# SWAPR provisioning repository

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

## Next steps
Here are a list of tasks that still need to be accomplished for this Docker environment.

- General
    - Use Docker secrets to pull out passwords
    - Make sure that that `config.json` located in `config/backend-config.json` is correct and can be used for all build configurations
    - Add appropriate environmental variables based on build configurations
    - Set secret key in backend config.json
- Production
    - Create `production.yml` for production settings
        - Make sure to use client `dist`
        - Use port `80` and `443` for nginx
    - Provision SSL certificate for `swapr.vip.gatech.edu` and add to the repo
- Development
    - Test and make sure that links between development code on the host work and can be used without trouble
        - Use client development build directory
    - Provision local self-signed SSL certificate for use during development
    - Set up proxy URL, something like `swapr.local` that proxies to `www:8080`
