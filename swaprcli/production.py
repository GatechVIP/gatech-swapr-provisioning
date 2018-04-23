import subprocess
import sys
import os

from cement.core.controller import CementBaseController, expose

from .config import PRODUCTION_DOCKER_IMAGES, PRODUCTION_STACK_NAME, PRODUCTION_DOCKER_ENV


class SwaprCLIProductionController(CementBaseController):
    class Meta:
        label = 'production'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Managing utilities for our production stack.'

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help="Deploys our stack to production.")
    def deploy(self):
        self.app.log.info("Deploying stack to production...")

        environment = os.environ.copy()
        environment.update(PRODUCTION_DOCKER_ENV)

        proc = subprocess.Popen(
            [
                'docker', 'stack', 'deploy',
                '-c', 'docker-compose.production.yaml',
                '--with-registry-auth',
                PRODUCTION_STACK_NAME
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
            env=environment
        )

        proc.communicate()

        if proc.returncode:
            self.app.log.error("Encountered error while deploying.")
        else:
            self.app.log.info("Production deployment succeeded.")

    @expose(help="Runs database migrations on the backend.")
    def migrate(self):
        self.app.log.info("Running database migrations...")

        environment = os.environ.copy()
        environment.update(PRODUCTION_DOCKER_ENV)

        service_name = '{}_backend'.format(PRODUCTION_STACK_NAME)

        proc = subprocess.Popen(
            [
                'docker', 'service', 'ps',
                '-f', "name={}.1".format(service_name),
                service_name,
                '-q', '--no-trunc',
            ],
            stdout=subprocess.PIPE,
            env=environment
        )

        container_name = proc.stdout.readline().decode('utf-8').strip()

        self.app.log.info("Found container: {}.1.{}".format(service_name, container_name))

        proc = subprocess.Popen(
            [
                'docker', 'exec',
                '{}.1.{}'.format(service_name, container_name),
                'sequelize', 'db:migrate'
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
            env=environment
        )

        proc.communicate()
